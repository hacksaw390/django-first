from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('customer', views.customer, name='customer'),
    path('product', views.product, name='product'),
    path('order', views.order, name='order'),
    path('register', views.register, name='register'),
    path('login', views.userLogin, name='login'),
    path('logout', views.logoutUser, name='logout'),
]
