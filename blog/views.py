from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from store.models import Category
from .models import Post
from SiteSettings.models import Setting

# Create your views here.


class PostView(ListView):
    model = Post
    template_name = 'blog.html'
    paginated_by = 10
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = Setting.objects.get(status=True)
        context['categories'] = Category.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog.html'
