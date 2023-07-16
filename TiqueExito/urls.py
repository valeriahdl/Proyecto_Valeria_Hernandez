from django.urls import path
from TiqueExito.views import *
from django.contrib.auth.views import *

urlpatterns = [

    path('winners/', winners, name ="winners"),
    path('landing/', landing, name ="landing"),
]