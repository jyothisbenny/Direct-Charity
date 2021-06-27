# Generated by Django 3.2.4 on 2021-06-23 17:07

import Patients.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patients', '0003_alter_patients_documents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='documents',
            field=models.FileField(upload_to='documents/%Y/%m/%d', validators=[Patients.validators.validate_file_extension]),
        ),
    ]
