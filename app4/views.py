from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def create_app(request):
    return HttpResponse('syntax:-  python manage.py startapp appname')
def after_this_process(request):
    return HttpResponse('Create views,then create urls,afterthat run the server whether the url is working fine or not,after that copy url and paste in browser and search.This will show u the content that u are written in views')
def process(request):
    return HttpResponse('We need to return HttpResponse.So u need to import HttpRespose from django.http(from django.http import HttpResponse)\nafter some process is there')