from django.db import models
from store.models import Product
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


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']


class Order(models.Model):
    pass
