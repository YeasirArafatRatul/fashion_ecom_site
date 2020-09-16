from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from accounts.models import User
from store.models import Product, Category
from .models import ShopCart, ShopCartForm
# Create your views here.


def order(request):
    return HttpResponse("Order Page")


@login_required(login_url='/login')  # Check login
def addtoshopcart(request, id):
    url = request.META.get("HTTP_REFERER")  # get last url
    current_user = request.user  # access user session info
    product = Product.objects.get(pk=id)
    checkproduct = ShopCart.objects.filter(
        product_id=id, user_id=current_user.id)
    if checkproduct:
        control = 1  # if the product is already in cart
    else:
        control = 0  # if the product is not in cart

# from detailview
    if request.method == "POST":
        form = ShopCartForm(request.POST)

        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.get(
                    product_id=id, user_id=current_user.id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Product Added to Cart")

        return HttpResponseRedirect(url)
# from home page
    else:  # if there is no post
        if control == 1:
            data = ShopCart.objects.get(product_id=id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
        messages.success(request, "Product Added To Cart")
    return HttpResponseRedirect(url)


def shopcart(request):
    category = Category.objects.all()
    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for p in shopcart:
        total += p.product.price * p.quantity
    # return HttpResponse(str(total))
    context = {'shopcart': shopcart,
               'category': category,
               'total': total,
               }
    return render(request, 'shopcart_products.html', context)
