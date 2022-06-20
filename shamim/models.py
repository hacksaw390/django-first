from django.db import models
# Create your models here.


class Contact(models.Model):
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.fname


class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class Product(models.Model):
    CATEGORY = (
        ('Indor', 'Indor'),
        ('Out dor', 'Out dor')
    )
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=50)
    category = models.CharField(max_length=100, choices=CATEGORY)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag, related_name='product_set')

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Out of delivered', 'Out of delivered')
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.customer.name


