
from django.shortcuts import render
from django.conf import settings
from .models import Setting, Slider
from django.views.generic.list import ListView
from store.models import Product
# Create your views here.


class ContactData(ListView):
    model = Setting
    template_name = 'contactus.html'


class About(ListView):
    model = Setting
    template_name = 'about.html'


def Home(request):
    setting = Setting.objects.get(id=1)
    sliding = Slider.objects.all
    latest_products = Product.objects.all().order_by('-id')[:8]
    context = {'setting': setting,
               'sliding': sliding,
               'latest': latest_products,

               }
    return render(request, 'home.html', context)
