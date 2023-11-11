from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages, auth
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def signin(request):
    if request.method == 'GET':
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

def go_to_form(request):
    if request.method == 'GET':
        return render(request, 'main.html')
    elif request.method == 'POST':
        return redirect('logout')