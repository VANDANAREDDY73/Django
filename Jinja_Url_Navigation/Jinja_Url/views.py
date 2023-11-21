from django.shortcuts import render

# Create your views here.
def python(request):
  return render(request,'python.html')
def functions(request):
  return render(request,'functions.html')