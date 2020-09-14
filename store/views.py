from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Category
from SiteSettings.models import Setting, Slider
from .forms import SearchForm
from django.db.models import Q
# Create your views here.


def category_products(request, id):
    categories = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    setting = Setting.objects.get(id=1)
    context = {
        'products': products,
        'categories': categories,
        'setting': setting,
    }
    return render(request, 'category.html', context)


def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = Product.objects.filter(
            Q(name__icontains=search_term)
        )

        setting = Setting.objects.get(id=1)
        categories = Category.objects.all()
        context = {
            'search_term': search_term,
            'products': search_results.filter(),
            'setting': setting,
            'categories': categories,
        }
        return render(request, 'search.html', context)

    else:
        return redirect('home')
