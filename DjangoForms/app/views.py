from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def djforms(request):
  ENFO=NameForm()
  d={'ENFO':ENFO}
  if request.method=='POST':
    NFO=NameForm(request.POST)
    if NFO.is_valid():
      return HttpResponse(str(NFO.cleaned_data))
  return render(request,'djforms.html',d)