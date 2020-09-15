from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def order(request):
    return HttpResponse("Order Page")
