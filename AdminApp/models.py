from django.db import models

# Create your models here.


class tbl_admin(models.Model):
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=15)