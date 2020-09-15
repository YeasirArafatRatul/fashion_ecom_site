from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Category
from SiteSettings.models import Setting, Slider
from .forms import SearchForm
from django.db.models import Q

# Create your views here.


class DetailsView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    # this function serves the product id
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)

    # this will server siteSettings data to this view
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = Setting.objects.get(status=True)
        return context


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
