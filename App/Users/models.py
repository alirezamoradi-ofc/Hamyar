from django.db import models
import uuid

# Create your models here.
class Student(models.Model):
   Name = models.CharField(max_length=100)
   Family = models.CharField(max_length=100)
   Father_Name = models.CharField(max_length=100)
   Birth_Day = models.DateField()

   def __str__(self):
      return self.Name