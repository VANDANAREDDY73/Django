from django.db import models

# Create your models here.
class Pyspiders(models.Model):
  Sname=models.CharField(max_length=100)
  Sid=models.IntegerField()
  address=models.TextField()
  email=models.EmailField(default='hi@gmail.com')
  remail=models.EmailField(default='hi@gmail.com')