from django.urls import path
from .views import *



urlpatterns = [
    path('registro/', user_create, name="registro" )
]
