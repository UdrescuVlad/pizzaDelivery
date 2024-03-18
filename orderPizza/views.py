from typing import Any
from django.db.models.base import Model as Model
from django.http import HttpResponseForbidden
from django.shortcuts import render
from .models import *
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
# Create your views here.

PIZZA_TYPE = ['Joshua', 'Happy']

class ViewPizzaMenu(ListView):
    model = Pizza
    context_object_name = 'pizzas'
    template_name = 'orderPizza/pizza_menu.html'
    def get_queryset(self) -> QuerySet[any]:
        return Pizza.objects.all()

class DetailedViewPizza(DetailView):
    model = Pizza
    context_object_name = 'pizza'
    def get_object(self):
        return Pizza.objects.get(pk=self.kwargs['pk'])
    
class FilterPizzaMenu(ListView):
    model = Pizza
    context_object_name = 'pizzas'
    template_name = 'orderPizza/pizza_menu.html'
    def get(self, request, *args, **kwargs):
        if not self.kwargs['pizzatype'] in PIZZA_TYPE:
            return render(request, 'orderPizza/404.html', {'error_message': 'This type of pizza is incorrect!'}, status=404)
    def get_queryset(self) -> QuerySet[Any]:
        return Pizza.objects.filter(pizza_type=self.kwargs['pizzatype'])

class ViewDailyMenu(ListView):
    model = DailyMenu
    context_object_name = 'menu'
    template_name = 'orderPizza/daily_menu.html'
    def get_queryset(self) -> QuerySet[any]:
        return DailyMenu.objects.all()
    
class DetailedViewDailyMenu(DetailView):
    model = DailyMenu
    context_object_name = 'dailyMenu'
    def get_object(self):
        return DailyMenu.objects.get(pk=self.kwargs['pk'])

    