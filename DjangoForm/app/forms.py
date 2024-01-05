from django import forms
from app.models import *

class topic(forms.Form):
  tname=forms.CharField()
class Webpage(forms.Form):
  tl=[[to.Topic_Name,to.Topic_Name] for to in Topic.objects.all()]
  tname=forms.ChoiceField(choices=tl)
  name=forms.CharField()
  url=forms.URLField()
  email=forms.EmailField()
class access_records(forms.Form):
  wl=[[wo.pk,wo.name] for wo in webpage.objects.all()]
  name=forms.ChoiceField(choices=wl)
  author=forms.CharField()
  date=forms.DateField()
