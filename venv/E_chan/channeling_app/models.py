from datetime import date
from tokenize import Name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Patient(models.Model):
    Name = models.CharField(max_length=60)
    Sex = models.CharField(max_length=10)
    Age = models.IntegerField()
    ContactNo = models.IntegerField(null=True)

class Appoinment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    Date_time=models.DateTimeField()
