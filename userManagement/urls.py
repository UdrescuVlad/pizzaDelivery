from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns=[
    path('login/', Login.as_view(), name='login.page'),
    path('logout/', Logout.as_view(), name='logout.page'),
]