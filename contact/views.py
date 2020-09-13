from django.shortcuts import render
from .models import ContactData
from django.views.generic.list import ListView
# Create your views here.


class ContactData(ListView):
    model = ContactData
    template_name = 'contactus.html'


def about(request):
    return render(request, template_name='about.html')
