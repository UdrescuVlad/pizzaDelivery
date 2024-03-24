from typing import Any
from django.db.models.base import Model as Model
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import *
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
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
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            rendered_template = render_to_string('orderPizza/404.html', {'error_message': 'This pizza index is not valid'})
            return HttpResponseNotFound(rendered_template)
    
class FilterPizzaMenu(ListView):
    model = Pizza
    context_object_name = 'pizzas'
    template_name = 'orderPizza/pizza_menu.html'
    def get(self, request, *args, **kwargs):
        if not self.kwargs['pizzatype'] in PIZZA_TYPE:
            rendered_template = render_to_string('orderPizza/404.html', {'error_message': 'This pizza filter is not valid'})
            return HttpResponseNotFound(rendered_template)
        else:
            return super().get(request, *args, **kwargs)
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
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            rendered_template = render_to_string('orderPizza/404.html', {'error_message': 'This daily meny is not valid'})
            return HttpResponseNotFound(rendered_template)