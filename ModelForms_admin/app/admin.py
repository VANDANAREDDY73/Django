from django.contrib import admin

# Register your models here.
from app.models import *
class Customizewebpage(admin.ModelAdmin):
  list_display=['Topic_Name','name','url']
  list_display_links=['url']
  list_editable=['name']
  list_filter=['email']
  list_per_page=1
  search_fields=['name']
admin.site.register(Topic)
admin.site.register(webpage,Customizewebpage)
admin.site.register(Access_Records)
admin.site.site_header='DJD'
admin.site.site_title='djando4:30'
admin.site.index_title='VANDU'