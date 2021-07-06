# Generated by Django 3.2.4 on 2021-07-03 04:26

import Patients.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=30)),
                ('patient_photo', models.FileField(upload_to='Images/%Y/%m/%d', validators=[Patients.validators.validate_file_extension_of_pic])),
                ('disease', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=400)),
                ('documents', models.FileField(upload_to='documents/%Y/%m/%d', validators=[Patients.validators.validate_file_extension])),
                ('doctor_name', models.CharField(max_length=30)),
                ('required_amount', models.IntegerField()),
                ('upi_id', models.CharField(max_length=50)),
                ('collected_amount', models.IntegerField(null=True)),
                ('admin_verified', models.BooleanField(default=False)),
                ('report_count', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patients.category')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patients.hospital')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=400)),
                ('documents', models.FileField(upload_to='ReportDocuments/%Y/%m/%d', validators=[Patients.validators.validate_file_extension])),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patients.patient')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('screenshot', models.FileField(upload_to='PaymentProofs/%Y/%m/%d', validators=[Patients.validators.validate_file_extension_of_pic])),
                ('admin_verified', models.BooleanField(default=False)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patients.patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='relationship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Patients.relationship'),
        ),
    ]
