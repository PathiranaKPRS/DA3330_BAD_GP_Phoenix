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
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Date_time=models.DateTimeField()
# Create your models here.
