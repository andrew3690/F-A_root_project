from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,RedirectView,ListView, DetailView
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from .forms import RegisterRun
from .models import Run

class LoginView(TemplateView):
    template_name='home/auth/login.html'

    def post(self, request,*args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            django_login(request,user)
            return render(request,'home/home.html')
        
        else:
            message='Invalid Credencials'
            return render(request,self.template_name,{'message':message})

class LogoutView(TemplateView):
    url='/login/'

    def get(self, request, *args, **kwargs):
        django_logout(request)
        return super().get(request, *args, **kwargs)

class RunListView(LoginRequiredMixin,ListView):
    template_name='run/overview.html'
    model = Run

class RunCreateView(LoginRequiredMixin,FormView,CreateView):
    template_name='run/createrun.html'
    form_class = RegisterRun

    def get_success_url(self) -> str:
        return reverse('orches:home')

class RunEditView(LoginRequiredMixin,FormView,UpdateView):
    template_name='run/updatetrun.html'
    form_class=RegisterRun

    def get_success_url(self) -> str:
        return reverse('orches:home')

class RunDeleteView(LoginRequiredMixin,DeleteView):
    template_name='run/deleterun.html'
    model=Run

    def get_success_url(self) -> str:
        return reverse('orches:home')