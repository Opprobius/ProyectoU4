from django.shortcuts import  redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, logout_then_login
from .forms import  NewUserForm
# Create your views here.


class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = NewUserForm

    def form_valid(self, form):
        form.save()
        return redirect('login')


class Login (LoginView):
    template_name ="registration/login.html"

