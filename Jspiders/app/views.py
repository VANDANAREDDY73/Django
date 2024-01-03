from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *
# Create your views here.
def djforms(request):
  EJO=Jspiders()
  d={'EJO':EJO}
  if request.method=='POST':
    JO=Jspiders(request.POST)
    if JO.is_valid():
      sn=JO.cleaned_data['Sname']
      si=JO.cleaned_data['Sid']
      a=JO.cleaned_data['address']
      NJO=Pyspiders.objects.get_or_create(Sname=sn,Sid=si,address=a)[0]
      NJO.save()
      return HttpResponse('Created')
    else:
      return HttpResponse('Not valid')
  return render(request,'djforms.html',d)