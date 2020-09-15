from django.contrib import admin
from .models import Category, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'new_price',
                    'old_price', 'updated_at', 'status', 'image_tag']
    list_filter = ['category', 'name', 'created_at']
    list_per_page = 15
    search_fields = ['category', 'name', 'new_price']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
