from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=14, unique=True)
    phone_verified = models.BooleanField(default=False)
    otp = models.IntegerField(null=True)
    is_admin = models.BooleanField(default=False)
