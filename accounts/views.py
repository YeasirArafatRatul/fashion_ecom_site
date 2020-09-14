from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.views.generic import CreateView
from SiteSettings.models import Setting


# Create your views here.


class SignUpView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = Setting.objects.get(id=1)
        return context
