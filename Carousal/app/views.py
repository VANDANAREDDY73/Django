from django.shortcuts import render

# Create your views here.
def carousal(request):
  return render(request,'carousal.html')