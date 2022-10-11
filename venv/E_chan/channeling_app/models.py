from datetime import date
from tokenize import Name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Doctor(models.Model):
    Name = models.CharField(max_length=40)
    Specialty = models.CharField(max_length=40)
    Reg_number = models.IntegerField()

class Patient(models.Model):
    Name = models.CharField(max_length=60)
    Sex = models.CharField(max_length=10)
    Age = models.IntegerField()
    ContactNo = models.IntegerField(null=True)

class Appoinment(models.Model):
    Name = models.CharField(max_length=60) 
    Phone =models.IntegerField(max_length=10)
    Email =models.EmailField(max_length=50)
    Address =models.CharField(max_length=80)
    