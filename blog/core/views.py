from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.views.generic import FormView, RedirectView

class LoginFormView(LoginView):
    template_name = 'base/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context

class LogoutView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)

def login(request):
     return render (request,"base/login.html")

def home(request):
     return render (request,"base/index.html")

def about(request):
     return render (request,"base/about.html")


def blog(request):
     return render (request,"base/blog.html")


def blogdetalle(request):
     return render (request,"base/blogdetalle.html")




def registrarse(request):
     return render (request,"base/registrarse.html")    