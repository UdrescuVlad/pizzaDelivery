from django.views.generic import TemplateView
from orderPizza.models import *
from django.views.generic import ListView
from django.db.models import Q

class HomeView(TemplateView):
    template_name = 'homepage/homepage.html'

class Search(ListView):
    template_name = 'homepage/search_page.html'
    context_object_name = 'list'

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            pizza_query_set = Pizza.objects.filter(
                Q(name__icontains=query)|
                Q(description__icontains=query)
            )
            daily_menus_query_set = DailyMenu.objects.filter(
                Q(first_course__icontains=query)|
                Q(second_course__icontains=query)
            )
            pizzas = list(pizza_query_set)
            daily_menus = list(daily_menus_query_set)

            # Combine the lists and make them distinct
            combined_results = pizzas + daily_menus
            combined_results = list(set(combined_results))
            return combined_results
        else:
            return Pizza.objects.none()