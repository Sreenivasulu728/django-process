from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def How_to_create_project(request):
    return HttpResponse('syntax:-  django-admin startproject projectname')