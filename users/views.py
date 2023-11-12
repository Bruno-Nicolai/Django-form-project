from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages, auth
from django.views.decorators.cache import never_cache
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

@never_cache
def signin(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('main')
        else:
            return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
            
        user = authenticate(username=username, password=pwd)
        if not user:
            messages.add_message(request, constants.ERROR, 'Invalid Login Credentials')
            return redirect(reverse('authentication'))
        login(request, user)
        return redirect('main')

def leave(request):
    logout(request),
    return redirect('authentication')
    
# def password_reset(request):
#     if request.method == 'GET':
#         return render(request, 'password_reset.html')

def go_to_form(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return redirect('authentication')
        else:
            return render(request, 'main.html')
    elif request.method == 'POST':
        return redirect('logout')