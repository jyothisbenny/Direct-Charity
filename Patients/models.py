from django.db import models
from django.conf import settings
from .validators import validate_file_extension, validate_file_extension_of_pic

User = settings.AUTH_USER_MODEL


# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Relationships(models.Model):
    relationship = models.CharField(max_length=30)

    def __str__(self):
        return self.relationship


class Hospitals(models.Model):
    hospital_name = models.CharField(max_length=100)
    place = models.CharField(max_length=30)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.hospital_name


class Patients(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    patient_name = models.CharField(max_length=30)
    relationship = models.ForeignKey(Relationships, on_delete=models.CASCADE)
    patient_photo = models.FileField(upload_to='Images/%Y/%m/%d', validators=[validate_file_extension_of_pic])
    disease = models.CharField(max_length=50)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    documents = models.FileField(upload_to='documents/%Y/%m/%d', validators=[validate_file_extension])
    hospital = models.ForeignKey(Hospitals, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=30)
    required_amount = models.IntegerField()
    upi_id = models.CharField(max_length=50)
    collected_amount = models.IntegerField(null=True)
    admin_verified = models.BooleanField(default=False)
