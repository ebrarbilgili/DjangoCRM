from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def home(request):
    customer = Customer.objects.all()
    order = Order.objects.all()

    total_customers = customer.count()

    total_orders = order.count()
    delivered = order.filter(status='Delivered').count()
    pending = order.filter(status='Pending').count()

    context = {'customers': customer, 'orders': order, 'total_customers': total_customers,
               'total_orders': total_orders, 'delivered': delivered, 'pending': pending}

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': products})


def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    total_order = orders.count()

    context = {'customer': customer,
               'orders': orders, 'total_order': total_order}
    return render(request, 'accounts/customer.html', context)
