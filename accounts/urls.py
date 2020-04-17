from django.urls import path
from .views import home, products, customers


urlpatterns = [
    path("", home),
    path("products/", products),
    path("customer/", customers),
]
