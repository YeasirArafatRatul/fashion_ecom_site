from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from SiteSettings.models import Setting
from accounts.models import User
from store.models import Product, Category
from .models import ShopCart, ShopCartForm
# Create your views here.




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
        print(url)
        return HttpResponseRedirect(url)
# from home page
    else:  # if there is no post
        if control == 1:
            data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
        messages.success(request, "Product Added To Cart")
        print(url)
    return HttpResponseRedirect(url)


def checkout(request):
    category = Category.objects.all()
    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    setting = Setting.objects.get(status=True)
    subtotal = 0
    for p in shopcart:
        subtotal += p.product.new_price * p.quantity

    delivery_charge = 50
    total = subtotal + delivery_charge
    # return HttpResponse(str(total))
    context = {'shopcart': shopcart,
               'category': category,
               'setting': setting,
               'sub_total': subtotal,
               'delivery_charge': delivery_charge,
               'total': total,
               }
    return render(request, 'checkout.html', context)


def deletefromcart(request, id):
    url = request.META.get("HTTP_REFERER")  # get last url
    ShopCart.objects.filter(id=id).delete()
    # messages.success(request, "Your item deleted form Shopcart.")
    return HttpResponseRedirect(url)


def placeorder(request):
   

    return HttpResponse('hello')
