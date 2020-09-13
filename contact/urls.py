from django.urls import path
from .views import ContactData
from .views import about


urlpatterns = [
    path('contact', ContactData.as_view(), name='contact'),
    path('about', about, name='about'),
]
