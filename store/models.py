from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Categories'

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=200)
    new_price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    old_price = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(
        max_length=200, default='', null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='products/')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" heights ="50" width="40" />'.format(self.image.url))
    image_tag.short_description = 'Image'

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
