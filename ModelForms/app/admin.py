from django.contrib import admin

# Register your models here.
from app.models import *


admin.site.register(Topic)
admin.site.register(webpage)
admin.site.register(Access_Records)