
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .models import Setting, Slider
from django.views.generic.base import TemplateView
from store.models import Product, Category
# Create your views here.


class ContactData(TemplateView):
    template_name = 'contactus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = Setting.objects.get(status=True)
        context['categories'] = Category.objects.all()
        return context


class About(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = Setting.objects.get(status=True)
        context['categories'] = Category.objects.all()
        return context


def Home(request):
    setting = Setting.objects.get(status=True)
    sliding = Slider.objects.filter(status=True)
    latest_products = Product.objects.all().order_by('-id')[:8]
    first_category = Product.objects.filter(category=1)
    # second_category = Product.objects.filter(category=2)
    # print(products_picked.id)
    random = Product.objects.all().order_by(
        '?')[:4]  # Random selected 4 products
    categories = Category.objects.all()
    context = {
        'setting': setting,
        'sliding': sliding,
        'latest': latest_products,
        'categories': categories,
        'first_category': first_category,
        'random': random

    }
    return render(request, 'home.html', context)


def allProducts(request):
    setting = Setting.objects.get(status=True)
    sliding = Slider.objects.filter(status=True)
    random = Product.objects.all().order_by(
        '?')[:28]  # Random selected 4 products
    categories = Category.objects.all()
    context = {
        'setting': setting,
        'sliding': sliding,
        'categories': categories,
        'all_products': random,

    }
    return render(request, 'all_products.html', context)
