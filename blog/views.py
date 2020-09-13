from django.shortcuts import render
from .models import Post
from django.views.generic.list import ListView
# Create your views here.


class PostView(ListView):
    model = Post
    template_name = 'blog.html'
    paginated_by = 10
