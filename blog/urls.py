from django.urls import path
from .views import PostView, PostDetailView


urlpatterns = [
    path('', PostView.as_view(), name='blog'),
    path('details/<int:id>', PostDetailView.as_view(), name='blog-details'),
]
