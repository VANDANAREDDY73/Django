from app2.views import *
from django.urls import path
app_name='program'
urlpatterns=[
  path('functions/',functions,name='functions')
]