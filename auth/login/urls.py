from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("users/", UsersAPI.as_view(), name='users'),
]