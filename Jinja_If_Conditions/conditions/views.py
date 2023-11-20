from django.shortcuts import render

# Create your views here.
def conditions(request):
  data={'a':50,'b':2000,'c':300}
  return render(request,'conditions.html',context=data)