from django.db import models
from django import forms
from store.models import Product
from accounts.models import User, UserProfile
from django.conf import settings
# Create your models here.


class ShopCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name

    # to show product price
    @property
    def price(self):
        return(self.product.new_price)

    # calculate_TOTAL
    @property
    def total(self):
        return(self.quantity*self.product.new_price)


class ShopCartForm(forms.ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']


# class Order(models.Model):
#     STATUS = (
#         ('New', 'New'),
#         ('Accepted', 'Accepted'),
#         ('Preaparing', 'Preaparing'),
#         ('OnShipping', 'OnShipping'),
#         ('Completed', 'Completed'),
#         ('Canceled', 'Canceled'),
#     )
#     Payment = (
#         ('CashOnDelivery', 'CashOnDelivery'),
#         ('bKash', 'bKash'),
#     )
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     code = models.CharField(max_length=5, editable=False)
#     first_name = models.CharField(max_length=10)
#     last_name = models.CharField(max_length=10)
#     phone = models.CharField(blank=True, max_length=20)
#     address = models.CharField(blank=True, max_length=150)
#     total = models.FloatField()
#     status = models.CharField(max_length=10, choices=STATUS, default='New')
#     payment_system = models.CharField(
#         max_length=10, choices=Payment, default='New')
#     adminnote = models.CharField(blank=True, max_length=100)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.user.first_name


# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = ['first_name', 'last_name',
#                   'address', 'phone', 'city', 'country']


# class OrderProduct(models.Model):
#     STATUS = (
#         ('New', 'New'),
#         ('Accepted', 'Accepted'),
#         ('Canceled', 'Canceled'),
#     )
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     price = models.FloatField()
#     amount = models.FloatField()
#     status = models.CharField(max_length=10, choices=STATUS, default='New')
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.product.title
