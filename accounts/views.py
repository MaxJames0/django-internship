from django.shortcuts import redirect, render
from django.views import View
from .forms import *
from .models import User
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DeleteView

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model, logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

user = get_user_model()


class RegisterView(CreateView):
    model = user
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    
    
class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home:index')


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')
    