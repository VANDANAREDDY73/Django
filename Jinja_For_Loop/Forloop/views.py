from django.shortcuts import render

# Create your views here.
def forloop(request):
  d={'Name':'Vandana'}
  
  return render(request,'forloop.html',d)