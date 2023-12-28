from django.db import models

# Create your models here.
class Topic(models.Model):
  Topic_Name=models.CharField(max_length=100,primary_key=True)
  def __str__(self):
    return self.Topic_Name

class webpage(models.Model):
  Topic_Name=models.ForeignKey(Topic,on_delete=models.CASCADE)
  name=models.CharField(max_length=100)
  url=models.URLField()
  email=models.EmailField()
  def __str__(self):
    return self.name
  
class Access_Records(models.Model):
  name=models.ForeignKey(webpage,on_delete=models.CASCADE)
  author=models.CharField(max_length=100)
  date=models.DateField()
  
