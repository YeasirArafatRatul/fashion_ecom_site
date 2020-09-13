from django.contrib import admin
from .models import Setting, Slider


class AdminContact(admin.ModelAdmin):
    list_display = ['id', 'sitePhone', 'siteEmail', 'siteAddress']


class AdminSlider(admin.ModelAdmin):
    list_display = ['id', 'status']


# Register your models here.
admin.site.register(Setting, AdminContact)
admin.site.register(Slider, AdminSlider)
