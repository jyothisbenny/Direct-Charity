# Generated by Django 3.2.5 on 2021-07-16 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patients', '0003_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='user_verified',
            field=models.BooleanField(default=False),
        ),
    ]