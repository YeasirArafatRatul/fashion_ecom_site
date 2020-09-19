from django.urls import path
<<<<<<< HEAD
from .views import addtoshopcart, checkout, deletefromcart, placeorder
urlpatterns = [

=======
from .views import placeorder, addtoshopcart, checkout, deletefromcart
urlpatterns = [
   
>>>>>>> 31892c8a57e4ad520a6bfbc299dde558b1d16099
    path('addtoshopcart/<int:id>', addtoshopcart, name='addtoshopcart'),
    path('deletefromcart/<int:id>', deletefromcart, name='deletefromcart'),
    path('checkout/', checkout, name='checkout'),
    path('placeorder', placeorder, name='placeorder'),
]
