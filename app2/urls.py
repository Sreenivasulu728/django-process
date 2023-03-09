from app2.views import *
from django.urls import path
app_name='app2'
urlpatterns=[
    path('create_VE_name/',create_VE_name,name='create_VE_name')
]