from django.db import models
from datetime import date
from tokenize import Name
from unittest.util import _MAX_LENGTH


# Create your models here.
class Doctor(models.Model):
    Name = models.CharField(max_length=40)
    Specialty = models.CharField(max_length=40)
    Reg_number = models.IntegerField()

    def __str__(self):
        return self.Name

class Patient(models.Model):
    Name = models.CharField(max_length=60)
    Sex = models.CharField(max_length=10)
    Age = models.IntegerField()
    ContactNo = models.IntegerField(null=True)

class Appoinment(models.Model):
    your_name=models.CharField(max_length=255, default="Phoenix")
    your_phone=models.IntegerField(default="0123456789")
    your_email=models.EmailField(max_length=255, default="Phoenix@gmail.com")
    your_address=models.CharField(max_length=255, default="Phoenix")
    your_schedule=models.CharField(max_length=255, default="Phoenix")
    your_date=models.CharField(max_length=255, default="Phoenix")
    your_message=models.TextField(max_length=255, default="Phoenix")
# Create your models here.
