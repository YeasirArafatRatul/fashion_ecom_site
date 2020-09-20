from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView

from .forms import RegisterForm
from django.views.generic.edit import CreateView
from SiteSettings.models import Setting
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from store.models import Category
from accounts.models import UserProfile

from .forms import UserUpdateForm, ProfileUpdateForm
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


@login_required(login_url='/login')
def profile(request):
    setting = Setting.objects.get(status=True)
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    print(profile.user.id)

    context = {'categories': category,
               'setting': setting,
               'profile': profile,
               }
    return render(request, 'user_profile.html', context)


@login_required(login_url='/login')
def user_update(request):

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, "Your Profile is updated successfully")
            return redirect('profile')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        setting = Setting.objects.get(status=True)
    context = {
        'categories': category,
        'user_form': user_form,
        'profile_form': profile_form,
        'setting': setting,

    }

    return render(request, 'user_update.html', context)


@login_required(login_url='/login')  # Check login
def password_change(request):
    url = request.META.get("HTTP_REFERER")
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            msg = messages.error(
                request, 'Error.<br>' + str(form.errors))
            return HttpResponseRedirect(url)
    else:
        category = Category.objects.all()
        setting = Setting.objects.get(status=True)
        form = PasswordChangeForm(request.user)
        return render(request, 'user_password.html', {'form': form, 'categories': category, 'setting': setting,
                                                      })
