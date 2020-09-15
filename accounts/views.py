from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.views.generic.edit import CreateView
from SiteSettings.models import Setting
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    success_message = "Registration Successful"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = Setting.objects.get(status=True)
        return context


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')
    success_message = "Welcome To Kazi Shop"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = Setting.objects.get(status=True)
        return context


class CustomLogoutView(LogoutView):
    def get_next_page(self):
        next_page = super(CustomLogoutView, self).get_next_page()
        messages.add_message(self.request, messages.SUCCESS,
                             'You Are Successfully Logged Out!')

        return next_page
