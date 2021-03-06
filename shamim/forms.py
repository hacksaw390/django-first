from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Contact, Customer, Product, Order


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class NewContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'