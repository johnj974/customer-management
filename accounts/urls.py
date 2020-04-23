from django.urls import path
from .views import home, products, customers, createOrder, updateOrder, deleteOrder, loginpage, register


urlpatterns = [
    path("", home, name="home"),
    path("products/", products, name="products"),
    path("customer/<str:pk>/", customers, name="customers"),
    path("create_order/<str:pk>/", createOrder, name="create_order"),
    path("update_order/<str:pk>/", updateOrder, name="update_order"),
    path("delete_order/<str:pk>/", deleteOrder, name="delete_order"),
    path("login/", loginpage, name="login"),
    path("register/", register, name="register"),
]
