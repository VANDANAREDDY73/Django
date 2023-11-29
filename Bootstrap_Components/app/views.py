from django.shortcuts import render

# Create your views here.
def bootstrap(request):
  return render(request,'bootstrap.html')
def components(request):
  return render(request,'components.html')
