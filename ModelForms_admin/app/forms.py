from django import forms 
from app.models import *
class TopicForm(forms.ModelForm):
  class Meta:
    model=Topic
    fields='__all__'
    labels={'Topic_Name':'TN'}

class WebpageForm(forms.ModelForm):
  class Meta:
    model=webpage
    fields='__all__'
    exclude=['url']
    widgets={'name':forms.Textarea()}

class AccessRecordsForm(forms.ModelForm):
  class Meta:
    model=Access_Records
    fields='__all__'