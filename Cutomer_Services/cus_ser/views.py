from multiprocessing import context
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.


def main(request):

    return render(request, 'main.html')


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    delivered = orders.filter(status='delivered').count()
    pending = orders.filter(status='pending').count()
    outForDelivery = orders.filter(status='outForDelivery').count()

    context = {'orders': orders,  'customers': customers,
               'total_orders': total_orders, 'delivered': delivered, 'pending': pending, 'outForDelivery': outForDelivery}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_order = customer.order_set.all().count()

    context = {'customer': customer,
               'orders': orders, 'total_order': total_order}
    return render(request, 'customers.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(
        Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'form': formset}
    return render(request, 'order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, "order_form.html", context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, "delete.html", context)


def register(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, "register.html", context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
