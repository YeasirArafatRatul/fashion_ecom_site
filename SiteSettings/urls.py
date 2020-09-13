from django.urls import path
from .views import Home, ContactData, About


urlpatterns = [
    path('', Home, name='home'),
    path('contact', ContactData.as_view(), name='contact'),
    path('about', About.as_view(), name='about'),
]
