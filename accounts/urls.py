from django.urls import path
from .views import home, products, customers, createOrder, updateOrder, deleteOrder, loginpage, register, logoutUser, userPage, accountSettings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path("products/", products, name="products"),
    path("customer/<str:pk>/", customers, name="customers"),
    path("create_order/<str:pk>/", createOrder, name="create_order"),
    path("update_order/<str:pk>/", updateOrder, name="update_order"),
    path("delete_order/<str:pk>/", deleteOrder, name="delete_order"),
    path("login/", loginpage, name="login"),
    path("logout/", logoutUser, name="logout"),
    path("register/", register, name="register"),
    path("user/", userPage, name="user_page"),
    path("account/", accountSettings, name="account"),
    path("reset_password/", auth_views.PasswordResetView.as_view(), name="reset_password"),
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
