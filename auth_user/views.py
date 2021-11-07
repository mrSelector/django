from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import FormView, CreateView

from auth_user.forms import CustomUserCreationForm
User = get_user_model()

class IndexView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'main_1.html', {'users': users})


class RegisterView(FormView):
    form_class = CustomUserCreationForm
    success_url = '/'
    template_name = 'register.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'login.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home'))
