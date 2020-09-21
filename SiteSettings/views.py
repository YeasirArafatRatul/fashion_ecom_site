
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
    sliding = Slider.objects.all
    latest_products = Product.objects.all().order_by('-id')[:8]
    first_category = Product.objects.filter(category=1)
    second_category = Product.objects.filter(category=2)
    # print(products_picked.id)
    categories = Category.objects.all()
    context = {
        'setting': setting,
        'sliding': sliding,
        'latest': latest_products,
        'categories': categories,
        'first_category': first_category,
        'second_category': second_category,

    }
    return render(request, 'home.html', context)
