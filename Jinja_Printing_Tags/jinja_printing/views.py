from django.shortcuts import render

# Create your views here.
def data_render(request):
  data = 'This data is our assumption'
  names='vandana'
  d={'assumption':data,'name':names}
  return render(request,'data_render.html',context=d)