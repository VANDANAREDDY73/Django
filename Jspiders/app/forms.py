from django import forms

def validate_for_a(data):
  if data.lower().startswith('a'):
    raise forms.ValidationError('Started with a')
class  Jspiders(forms.Form):
  Sname=forms.CharField(validators=[validate_for_a])
  Sid=forms.IntegerField()
  address=forms.CharField(widget=forms.Textarea)
  email=forms.EmailField()
  remail=forms.EmailField()

  def clean(self):
    e=self.cleaned_data['email']
    r=self.cleaned_data['remail']
    if e!=r:
      raise forms.ValidationError('Emails not matched')