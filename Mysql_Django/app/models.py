from django.db import models

# Create your models here.
class School(models.Model):
  Sname=models.CharField(max_length=100)
  Sprincipal=models.CharField(max_length=100)
class Student(models.Model):
  Stname=models.CharField(max_length=100)
  Sname=models.ForeignKey(School,on_delete=models.CASCADE)
  