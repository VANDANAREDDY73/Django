from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def topics(request):
  ETO=topic()
  d={'ETO':ETO}
  if request.method=='POST':
    TO=topic(request.POST)
    if TO.is_valid():
      tn=TO.cleaned_data['tname']
      qto=Topic.objects.get_or_create(Topic_Name=tn)[0]
      qto.save()
      return HttpResponse('created')
    else:
      return HttpResponse('not valid')
  return render(request,'topics.html',d)

def webpages(request):
  EWO=Webpage()
  d={'EWO':EWO}
  if request.method=='POST':
    WO=Webpage(request.POST)
    if WO.is_valid():
      tn=WO.cleaned_data['tname']
      n=WO.cleaned_data['name']
      ur=WO.cleaned_data['url']
      em=WO.cleaned_data['email']
      TO=Topic.objects.get(Topic_Name=tn)
      qwo=webpage.objects.get_or_create(Topic_Name=TO,name=n,url=ur,email=em)[0]
      qwo.save()
      return HttpResponse('created')
    else:
      return HttpResponse('invalid')

  return render(request,'webpages.html',d)


def access(request):
  EAO=access_records()
  d={'EAO':EAO}
  if request.method=='POST':
    AO=access_records(request.POST)
    if AO.is_valid():
      n=AO.cleaned_data['name']
      WO=webpage.objects.get(pk=n)
      a=AO.cleaned_data['author']
      d=AO.cleaned_data['date']
      QAO=Access_Records.objects.get_or_create(name=WO,author=a,date=d)[0]
      QAO.save()
      return HttpResponse('Created')
    else:
      return HttpResponse('Not valid')
  return render(request,'access.html',d)
