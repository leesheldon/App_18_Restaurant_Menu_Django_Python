from django.shortcuts import render
from django.views import generic
from .models import Meal, MEAL_TYPE


class MenuList(generic.ListView):
    queryset = Meal.objects.order_by("-created_on")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meal_types"] = MEAL_TYPE
        return context


class MenuItemDetail(generic.DetailView):
    model = Meal
    template_name = "menu_item_detail.html"










































