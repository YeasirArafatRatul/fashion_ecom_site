from django.urls import path
from .views import order, addtoshopcart, checkout, deletefromcart
urlpatterns = [
    path('', order, name='order'),
    path('addtoshopcart/<int:id>', addtoshopcart, name='addtoshopcart'),
    path('deletefromcart/<int:id>', deletefromcart, name='deletefromcart'),
    path('checkout/', checkout, name='checkout')
]
