from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.


class UsersProfile(AbstractUser):
  phone = models.CharField(max_length=14)
  phone_verified = models.BooleanField(default=False)
  otp = models.IntegerField(max_length=6, null=True)
