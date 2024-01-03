from django import forms
class  Jspiders(forms.Form):
  Sname=forms.CharField()
  Sid=forms.IntegerField()
  address=forms.CharField(widget=forms.Textarea)