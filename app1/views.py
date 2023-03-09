from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def how_to_install_VE(request):
    return HttpResponse('syntax:-  pip install virtualenv')