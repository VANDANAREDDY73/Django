from django import forms
g=[['FEMALE','Female'],['MALE','MALE']]
c=[['PYTHON','PYTHON'],['DJANGO','DJANGO'],['SQL','SQL']]
class NameForm(forms.Form):
  Sname=forms.CharField()
  Sage=forms.IntegerField()
  #Gender=forms.ChoiceField(choices=g)
  #Gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
  #Scourse=forms.MultipleChoiceField(choices=c)
  Scourse=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
  Address=forms.CharField(widget=forms.Textarea(attrs={'cols':5,'rows':5}))