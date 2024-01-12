from django.shortcuts import render
import datetime
# Create your views here.
def filters(request):
  dt=datetime.datetime.now
  d={'data':'Python Is A HiGh LeVeL PROGRaMMING lANGUaGE','dt':dt,'c':2}
  return render(request,'filters.html',d)