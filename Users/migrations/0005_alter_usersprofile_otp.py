# Generated by Django 3.2.4 on 2021-06-08 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_alter_usersprofile_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersprofile',
            name='otp',
            field=models.IntegerField(max_length=6, null=True),
        ),
    ]
