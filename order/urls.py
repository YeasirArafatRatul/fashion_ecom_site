from django.urls import path
from .views import addtoshopcart, checkout, deletefromcart, placeorder
urlpatterns = [

    path('addtoshopcart/<int:id>', addtoshopcart, name='addtoshopcart'),
    path('deletefromcart/<int:id>', deletefromcart, name='deletefromcart'),
    path('checkout/', checkout, name='checkout'),
    path('placeorder', placeorder, name='placeorder'),
]
