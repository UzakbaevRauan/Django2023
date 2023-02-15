from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegisterForm
from .models import User



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('store:products'))
    else:
        form= UserLoginForm()

    context = {'form':form}
    return render(request,'users/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
        context = {'form':form}
        return render(request, 'users/register.html',context)