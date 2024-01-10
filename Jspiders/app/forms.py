from django import forms
from django.core import validators
def validate_for_a(data):
  if data.lower().startswith('a'):
    raise forms.ValidationError('Started with a')
class  Jspiders(forms.Form):
  Sname=forms.CharField(validators=[validate_for_a,validators.MinLengthValidator(4)])
  Sid=forms.IntegerField()
  address=forms.CharField(widget=forms.Textarea)
  email=forms.EmailField()
  remail=forms.EmailField()
  botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)
  def clean_botcatcher(self):
    b=self.cleaned_data['botcatcher']
    if len(b)>0:
      raise forms.ValidationError('Bot')
  def clean(self):
    e=self.cleaned_data['email']
    r=self.cleaned_data['remail']
    s=self.cleaned_data['Sname']
    i=self.cleaned_data['Sid']
    if e!=r:
      raise forms.ValidationError
    