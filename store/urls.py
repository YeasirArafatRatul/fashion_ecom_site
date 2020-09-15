
from django.urls import path
from .views import category_products
from .views import DetailsView
urlpatterns = [
    path('category/<int:id>/', category_products, name='category'),
    path('detail/<int:id>/', DetailsView.as_view(), name='detail'),

]
