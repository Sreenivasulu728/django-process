from app3.views import *
from django.urls import path
app_name='app3'
urlpatterns = [
    path('How_to_create_project/',How_to_create_project,name='How_to_create_project')
]
