from django.shortcuts import render, redirect
from .models import Contact, Customer, Product, Order
from .forms import CustomerForm, ProductForm, OrderForm, UserRegisterForm
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorator import check_authenticated


@check_authenticated
def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Register success ' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, 'auth/register.html', context)


@check_authenticated
def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password wrong!')

    context = {}
    return render(request, 'auth/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'home/home.html')


@login_required(login_url='login')
def about(request):

    data = Contact.objects.all()

    context = {
        "data": data
    }
    return render(request, 'about/about.html', context)


@login_required(login_url='login')
def customer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer')

    customers = Customer.objects.order_by('-id')
    context = {
        'form': form,
        'customers': customers
    }
    return render(request, 'ecom/customer.html', context)


@login_required(login_url='login')
def product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
    products = Product.objects.order_by('-id').values()
    tag_products = Product.objects.filter(category='indor').order_by('id')
    context = {
        'form': form,
        'products': products,
        'tag_products': tag_products
    }
    return render(request, 'ecom/product.html', context)


@login_required(login_url='login')
def order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order')

    orders = Order.objects.order_by('-id')
    pending_orders = Order.objects.filter(status='Pending').order_by('customer__name')
    delivered_orders = Order.objects.filter(status='Delivered').order_by('customer__name')
    context = {
        'form': form,
        'orders': orders,
        'pending_orders': pending_orders,
        'delivered_orders': delivered_orders
    }
    return render(request, 'ecom/order.html', context)