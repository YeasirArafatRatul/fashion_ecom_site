from django.contrib import admin
from .models import ContactData


class AdminContact(admin.ModelAdmin):
    list_display = ['id', 'phone', 'address', 'email']


# Register your models here.
admin.site.register(ContactData, AdminContact)
