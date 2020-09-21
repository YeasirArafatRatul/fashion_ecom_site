from django.contrib import admin
from django.contrib.auth.admin import Group
from django.contrib.auth import get_user_model
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'datetime')
    list_filter = ('title', 'datetime')

    search_fields = ('title', 'description',)


admin.site.register(Post, PostAdmin)
