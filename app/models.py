from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django import forms

# Create your models here.
class Donor(models.Model):
    id = models.BigAutoField(primary_key = True)
    full_name = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 10)
    age = models.IntegerField()
    blood_grp = models.CharField(max_length = 5)
    country = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    phno = models.IntegerField()
    file = models.FileField(upload_to = "uploads/")
    any_disease = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.full_name
    


class DonorRegister(models.Model):
    full_name = models.CharField(max_length = 30)
    email = models.EmailField(default="xyz@gmail.com", max_length = 254, unique = True)
    password = models.CharField(max_length = 30)

    def __str__(self) -> str:
        return self.full_name   
