from django.urls import path
from .views import home, products, customers, createOrder, updateOrder


urlpatterns = [
    path("", home, name="home"),
    path("products/", products, name="products"),
    path("customer/<str:pk>/", customers, name="customers"),
    path("create_order/", createOrder, name="create_order"),
    path("update_order/<str:pk>/", updateOrder, name="update_order"),
]
