from django.contrib import admin
<<<<<<< HEAD
from .models import ShopCart
=======
>>>>>>> 31892c8a57e4ad520a6bfbc299dde558b1d16099
from .models import ShopCart, Order, OrderProduct


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product',
                    'quantity', 'price', 'total']
    list_filter = ['user']


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['code', 'user', 'full_name',
                    'phone', 'city', 'total', 'status']
=======
    list_display = ['user', 'full_name', 'phone', 'city', 'total', 'status']
>>>>>>> 31892c8a57e4ad520a6bfbc299dde558b1d16099
    list_filter = ['status']
    readonly_fields = ('user', 'first_name', 'last_name',
                       'address', 'city', 'phone', 'total')
    can_delete = False
    inlines = [OrderProductInline]


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter = ['user']


# Register your models here.
admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
<<<<<<< HEAD
=======

>>>>>>> 31892c8a57e4ad520a6bfbc299dde558b1d16099
