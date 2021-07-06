from django.db import models
from django.conf import settings
from .validators import validate_file_extension, validate_file_extension_of_pic

from django.utils.timezone import now

User = settings.AUTH_USER_MODEL


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Relationship(models.Model):
    relationship = models.CharField(max_length=30)

    def __str__(self):
        return self.relationship


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    place = models.CharField(max_length=30)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.hospital_name + ", " + self.place + ", " + self.district


class Patient(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=30)
    relationship = models.ForeignKey(Relationship, on_delete=models.CASCADE)
    patient_photo = models.FileField(upload_to='Images/%Y/%m/%d', validators=[validate_file_extension_of_pic])
    disease = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    documents = models.FileField(upload_to='documents/%Y/%m/%d', validators=[validate_file_extension])
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=30)
    required_amount = models.IntegerField()
    upi_id = models.CharField(max_length=50)
    collected_amount = models.IntegerField(default=0)
    admin_verified = models.BooleanField(default=False)
    report_count = models.IntegerField(default=0)


class Payment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField(default=now)
    screenshot = models.FileField(upload_to='PaymentProofs/%Y/%m/%d', validators=[validate_file_extension_of_pic])
    admin_verified = models.BooleanField(default=False)


class Report(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    documents = models.FileField(upload_to='ReportDocuments/%Y/%m/%d', validators=[validate_file_extension])


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

