from django.shortcuts import render

# Create your views here.
def userfilters(request):
  d={'data':'Python IS A HigH LevEL ProGraMming LanGUage'}
  return render(request,'userfilters.html',d)