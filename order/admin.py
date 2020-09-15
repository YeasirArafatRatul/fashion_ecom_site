from django.contrib import admin
from .models import ShopCart


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product',
                    'quantity', 'price', 'total']
    list_filter = ['user']


# Register your models here.
admin.site.register(ShopCart, ShopCartAdmin)
