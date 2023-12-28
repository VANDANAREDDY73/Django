from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def Topics(request):
  if request.method=='POST':
    tno=request.POST['tn']
    TOP=Topic.objects.get_or_create(Topic_Name=tno)[0]
    TOP.save()
    QTO=Topic.objects.all()
    d1={'topics':QTO}
    return render(request,'display_topic.html',d1)
  return render(request,'Topics.html')


def insert_webpage(request):
  QLTO=Topic.objects.all()
  d={'topics':QLTO}
  if request.method=='POST':
    tn=request.POST['tn']
    na=request.POST['na']
    ur=request.POST['ur']
    em=request.POST['em']
    TO=Topic.objects.get(Topic_Name=tn)
    wo=webpage.objects.get_or_create(Topic_Name=TO,name=na,url=ur,email=em)[0]
    wo.save()
    QWO=webpage.objects.all()
    d1={'webpages':QWO}
    return render(request,'display_webpage.html',d1)



  return render(request,'insert_webpage.html',d)


def insert_access(request):
  WO=webpage.objects.all()
  d={'access':WO}
  if request.method=='POST':
    na=request.POST['na']
    au=request.POST['au']
    da=request.POST['da']
    wto=webpage.objects.get(pk=na)
    AO=Access_Records.objects.get_or_create(name=wto,author=au,date=da)[0]
    AO.save()
    QAO=Access_Records.objects.all()
    d1={'records':QAO}
    return render(request,'display_access.html',d1)
    
  return render(request,'insert_access.html',d)