"""pizzaDelivery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from orderPizza.views import *

urlpatterns = [
    path('pizza/', ViewPizzaMenu.as_view(), name="pizza.menu"),
    path('pizza/<int:pk>/', DetailedViewPizza.as_view(), name="pizza.detail"),
    path('pizza/filter/<str:pizzatype>/', FilterPizzaMenu.as_view(), name='pizza.filter'),
    path('daily/', ViewDailyMenu.as_view(), name="daily.menu"),
    path('daily/<int:pk>/', DetailedViewDailyMenu.as_view(), name='daily.menu.detail'),
]
