from django.urls import path
from django.conf import settings
from .views import SignUpView, CustomLogoutView, CustomLoginView, profile, user_update, password_change
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    #     the below path can also be used
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #     path('register/', SignUpView.as_view(),
    #          {'next_page': 'login'}, name='register'),
    #     path('login/', CustomLoginView.as_view(),
    #          {'next_page': settings.LOGIN_REDIRECT_URL}, name='login'),
    path('logout/', CustomLogoutView.as_view(),
         {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('profile/', profile, name='profile'),
    path('update/', user_update, name='update'),
    path('password/', password_change, name='password'),
]
