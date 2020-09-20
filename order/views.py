from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.urls import reverse

from SiteSettings.models import Setting
from accounts.models import User
from store.models import Product, Category
from .models import ShopCart, ShopCartForm, OrderForm, OrderProduct, Order
from accounts.models import UserProfile
# Create your views here.

# Check login


def addtoshopcart(request, id):
    url = request.META.get("HTTP_REFERER")  # get last url
    current_user = request.user  # access user session info
    product = Product.objects.filter(pk=id).first()
    print(product)
    # jehetu ekhane product query kore ansi, eta safe jodio same kotha
    if product:
        checkproduct = ShopCart.objects.filter(
            product=product, user_id=current_user.id)
        if checkproduct:
            control = 1  # if the product is already in cart
        else:
            control = 0  # if the product is not in cart

    # from detailview
        if request.method == "POST":
            form = ShopCartForm(request.POST)

            if form.is_valid():
                if control == 1:
                    data = ShopCart.objects.filter(
                        product=product, user_id=current_user.id).first()
                    if data:
                        data.quantity += form.cleaned_data['quantity']
                        data.product = product
                        data.save()
                else:
                    data = ShopCart()
                    data.user_id = current_user.id
                    data.product = product
                    data.quantity = form.cleaned_data['quantity']
                    data.save()
            messages.success(request, "Product Added to Cart")
            return HttpResponseRedirect(url)

    # from home page
        else:  # if there is no post
            if control == 1:
                data = ShopCart.objects.filter(
                    product_id=id, user_id=current_user.id).first()
                # print(data.quantity, 'productsss')
                if data:
                    # in that we didnot save the (data.product = product) before
                    data.product = product
                    data.quantity += 1
                    data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = 1
                data.save()
            messages.success(request, "Product Added To Cart")

        return HttpResponseRedirect(url)
    else:
        # some operation
        pass


@login_required(login_url='login')
def checkout(request):
    category = Category.objects.all()
    setting = Setting.objects.get(status=True)

    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    # for item in shopcart:
    #     print(item.id)

    subtotal = 0
    for p in shopcart:
        subtotal += p.product.new_price * p.quantity

    delivery_charge = 50
    total = subtotal + delivery_charge

    context = {'shopcart': shopcart,
               'categories': category,
               'setting': setting,
               'sub_total': subtotal,
               'delivery_charge': delivery_charge,
               'total': total,

               }

    return render(request, 'checkout.html', context)


@login_required(login_url='login')
def deletefromcart(request, id):
    url = request.META.get("HTTP_REFERER")  # get last url
    ShopCart.objects.filter(id=id).delete()
    # messages.success(request, "Your item deleted form Shopcart.")
    return HttpResponseRedirect(url)


# ORDER

@login_required(login_url='login')
def placeorder(request):
    category = Category.objects.all()
    setting = Setting.objects.get(status=True)
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    profile = UserProfile.objects.get(user_id=current_user.id)
    total = 0
    subtotal = 0
    for p in shopcart:
        subtotal += p.product.new_price * p.quantity

    delivery_charge = 50
    total = subtotal + delivery_charge

    # for rs in shopcart:
    #     if rs.product.variant == 'None':
    #         total += rs.product.price * rs.quantity
    #     else:
    #         total += rs.variant.price * rs.quantity

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total

            ordercode = "KF-" + get_random_string(5).upper()
            data.code = ordercode
            data.save()

            for rs in shopcart:
                detail = OrderProduct()
                detail.order_id = data.id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                detail.price = rs.product.new_price
                # detail.variant_id = rs.variant_id
                detail.amount = rs.product.new_price * rs.quantity
                detail.save()

            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items'] = 0
            messages.success(
                request, "Your Order has been placed. Thank you.")
            url = reverse('home')
            return HttpResponseRedirect(url)
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("home")

    form = OrderForm()
    context = {'shopcart': shopcart,
               'categories': category,
               'setting': setting,
               'total': total,
               'form': form,
               'profile': profile,
               }
    return render(request, 'order_Form.html', context)
