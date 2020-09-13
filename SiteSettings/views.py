
from django.shortcuts import render
from django.conf import settings
from .models import Setting, Slider
from django.views.generic.list import ListView
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

    context = {'setting': setting,
               'sliding': sliding,

               }
    return render(request, 'home.html', context)
