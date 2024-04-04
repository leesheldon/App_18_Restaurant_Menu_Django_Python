from django.shortcuts import render
from django.views import generic
from .models import Meal


class MenuList(generic.ListView):
    queryset = Meal.objects.order_by("-created_on")
    template_name = "index.html"


class MenuItemDetail(generic.DetailView):
    model = Meal
    template_name = "menu_item_detail.html"

