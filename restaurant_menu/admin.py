from django.contrib import admin
from .models import Meal


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal_name", "meal_type", "status")
    list_filter = ("status", "meal_type")
    search_fields = ("meal_name", "description")


admin.site.register(Meal, MenuItemAdmin)
