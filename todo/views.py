from django.shortcuts import render
# HttpResponseを呼び出す
from django.http import HttpResponse

# Create your views here.

# urls.pyで定義したtodoをviews.pyに紐付け(定義)する
def todo(request):
  return HttpResponse('')