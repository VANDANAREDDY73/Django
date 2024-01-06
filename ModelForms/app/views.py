from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
  ETFO=TopicForm()
  d={'ETFO':ETFO}
  if request.method=='POST':
    TFO=TopicForm(request.POST)
    if TFO.is_valid():
      TFO.save()
      return HttpResponse('Inserted Successfully')

  return render(request,'insert_topic.html',d)

def insert_webpage(request):
  EWFO=WebpageForm()
  d={'EWFO':EWFO}
  if request.method=='POST':
    WFO=WebpageForm(request.POST)
    if WFO.is_valid():
      WFO.save()
      return HttpResponse('Inserted Successfully')
  return render(request,'insert_webpage.html',d)

def insert_access(request):
  EAFO=AccessRecordsForm()
  d={'EAFO':EAFO}
  if request.method=='POST':
    AFO=AccessRecordsForm(request.POST)
    if AFO.is_valid():
      AFO.save()
      return HttpResponse('Inserted Successfully')
  return render(request,'insert_access.html',d)