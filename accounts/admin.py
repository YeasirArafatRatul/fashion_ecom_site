from django.contrib import admin
from django.contrib.auth.admin import Group
from django.contrib.auth import get_user_model
from .models import User, UserProfile
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone')
    list_filter = ('username', 'email', 'phone')

    search_fields = ('email', 'username',)


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
admin.site.unregister(Group)
