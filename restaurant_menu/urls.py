from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    path('item/<int:pk>/<str:meal_type_value>/', views.MenuItemDetail.as_view(), name="menu_item")
]
