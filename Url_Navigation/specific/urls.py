from specific.views import *
from django.urls import path
app_name='specific'

urlpatterns=[
  path('sql/',sql,name='sql')
]