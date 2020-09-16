from django.urls import path
from .views import order, addtoshopcart
urlpatterns = [
    path('', order, name='order'),
    path('addtoshopcart/<int:id>', addtoshopcart, name='addtoshopcart')
]
