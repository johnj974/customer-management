from django.shortcuts import render, redirect, reverse
from .models import Customer, Product, Order
from .forms import OrderForm


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()
    context = {"orders": orders, "customers": customers, "total_customers": total_customers,
    "total_orders": total_orders, "delivered": delivered, "pending": pending}
    return render(request, "accounts/dashboard.html", context,)


def products(request):
    products = Product.objects.all()
    return render(request, "accounts/products.html", {"products": products})


def customers(request, pk):
    customers = Customer.objects.get(id=pk)
    orders = customers.order_set.all()
    order_count = orders.count()
    context = {"customers": customers, "orders": orders, "order_count": order_count}
    return render(request, "accounts/customer.html", context)


def createOrder(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "accounts/order_form.html", context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    context = {"form": form}
    return render(request, "accounts/order_form.html", context)


