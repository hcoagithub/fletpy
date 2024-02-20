from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('registro/', user_create, name="registro" )
]
