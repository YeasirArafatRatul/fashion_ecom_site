
from django.urls import path
from .views import category_products
urlpatterns = [
    path('category/<int:id>/', category_products, name='category'),

]
