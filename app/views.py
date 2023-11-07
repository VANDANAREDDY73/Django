from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def JamPandu(request):
  return HttpResponse('Hi JamPandu How Are You')


def JigelRani(request):
  return HttpResponse('Hi JigelRani')
