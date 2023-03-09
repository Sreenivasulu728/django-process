from app1.views import *
from django.urls import path
app_name='app1'
urlpatterns=[
    path('how_to_install_VE',how_to_install_VE,name='how_to_install_VE')
]