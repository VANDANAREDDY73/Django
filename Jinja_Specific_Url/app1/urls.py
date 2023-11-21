from app1.views import *
from django.urls import path
app_name='code'
urlpatterns=[
  path('python/',python,name='python')
]