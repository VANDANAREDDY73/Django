from django.db import models

# Create your models here.
class country(models.Model):
  COUNTRY_NAME = models.CharField(max_length=100,primary_key=True)
  def __str__(self):
    return self.COUNTRY_NAME
class capital(models.Model):
  COUNTRY_NAME = models.OneToOneField(country,on_delete=models.CASCADE)
  CAPITAL_NAME = models.CharField(max_length=200)
  def __str__(self):
    return self.CAPITAL_NAME