from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def create_student(request):
  ESO=StudentForm()
  d={'ESO':ESO}
  if request.method=='POST':
    SO=StudentForm(request.POST)
    if SO.is_valid():
      SO.save()
      return HttpResponse('Created')
    else:
      return HttpResponse('Invalid')
  return render(request,'create_student.html',d)