from app4.views import *
from django.urls import path
app_name='app4'
urlpatterns = [
    path('create_app/',create_app,name='create_app'),
    path('after_this_process/',after_this_process,name='after_this_process'),
    path('process/',process,name='process'),
]
