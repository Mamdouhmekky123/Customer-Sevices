import email
from itertools import product
from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=100, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (('in door', 'in door'),
                ('out door', 'out door'),
                )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(max_length=20, null=True)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    describtion = models.CharField(max_length=100, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (('pending', 'pending'),
              ('outForDelivery', 'outForDelivery'),
              ('delivered', 'delivered'),
              )
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name
