from re import template
from django.shortcuts import render, redirect
from .models import Contact, Customer, Product, Order, Contact
from .forms import CustomerForm, ProductForm, OrderForm, UserRegisterForm, ContactForm, NewContactForm
from django.http import HttpResponse
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorator import check_authenticated
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView, ListView, DeleteView


class NewContactView(FormView):
    form_class = NewContactForm
    template_name = 'contact/new-contact.html'
    # success_url = 'new-contact'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contact.objects.order_by('-id')
        return context

    def get_success_url(self):
        return reverse_lazy('new-contact')


class HomeView(TemplateView):
    template_name = 'generic/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = 'ago'
        return context


class NewContact(View):
    form_class = NewContactForm
    template = 'contact/new-contact.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request,self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new-contact')


def contact(request):
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    contacts = Contact.objects.order_by('-id')
    context = {'form': form, 'contacts': contacts}
    return render(request, 'contact/contact.html',context)


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


class ContactListView(ListView):
    template_name = 'about/about.html'
    model = Product
    # context_object_name = 'contacts'
    # queryset = Contact.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Product.objects.all()
        context['msg'] = 'hi'
        return context


class ProductDetailView(DeleteView):
    template_name = 'about/product-detail.html'
    model = Product
    context_object_name = 'product'


@login_required(login_url='login')
def about(request):

    data = Contact.objects.all()

    context = {
        "data": data
    }
    return render(request, 'about/about.html', context)


class CustomerCreateView(CreateView):
    form_class = CustomerForm
    template_name = 'ecom/customer.html'
    success_url = 'customer'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.order_by('-id')
        return context


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