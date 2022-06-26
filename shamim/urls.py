from django.urls import path
from . import views
from .views import NewContact, HomeView, NewContactView, CustomerCreateView, ContactListView, \
    ProductDetailView, ProductUpdateView, ProductDeleteView, tagProduct, CategoryProduct
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),

    # path('about', views.about, name='about'),
    path('about', ContactListView.as_view(), name='about'),
    path('product-detail/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('product-edit/<int:pk>', ProductUpdateView.as_view(), name='product-edit'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),

    # path('tag-product/<int:pk>', views.tagProduct, name='tag-product'),
    path('tag-product/<int:pk>', tagProduct.as_view(), name='tag-product'),
    path('category-product/<str:category>', CategoryProduct.as_view(), name='category-product'),

    path('customer', CustomerCreateView.as_view(), name='customer'),
    # path('customer', views.customer, name='customer'),

    path('product', views.product, name='product'),


    path('order', views.order, name='order'),
    path('register', views.register, name='register'),
    path('login/', views.userLogin, name='login'),
    path('logout', views.logoutUser, name='logout'),


    path('contact', views.contact, name='contact'),
    path('new-contact', NewContactView.as_view(), name='new-contact'),


    # path('t-view', TemplateView.as_view(template_name = 'generic/home.html'), name='t-view'),
    path('t-view', HomeView.as_view(), name='t-view'),
]
