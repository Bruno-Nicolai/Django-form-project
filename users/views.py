from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages, auth
from django.core.mail import send_mail
from django.views.decorators.cache import never_cache
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from decouple import config

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

def go_to_form(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return redirect('authentication')
        else:
            return render(request, 'main.html')
    elif request.method == 'POST':
        return redirect('logout')
    
# ===========================================================    

def build_message(request):
    trav_name = request.POST.get('username')
    trav_purpose = request.POST.get('purpose')
    meet = request.POST.get('meeting')
    time_start = request.POST.get('f_conf_st_time')
    date_start = request.POST.get('date_f_conf_start')
    time_end = request.POST.get('l_conf_nd_time')
    date_end = request.POST.get('date_l_conf_end')
    dest_from = request.POST.get('from_dest')
    dest_to = request.POST.get('to_dest')
    textarea_one = request.POST.get('tarea_i')
    textarea_two = request.POST.get('tarea_ii')
    textarea_three = request.POST.get('tarea_iii')

    user_email = request.user.username if request.user.is_authenticated else '' 
    
    traveler_info = f'{trav_name} ({user_email})'

    return {
        'email_subject': f'{traveler_info} has requested approval for the travel below. Please approve or reject the requested trip.',
                
        'email_message': f'''
        Traveler Name: {trav_name}
        Purpose: {trav_purpose}
        Meeting: {meet}
        First Meeting/Conference Start Date: {date_start}
        First Meeting/Conference Start Time: {time_start}
        Last Meeting/Conference End Date: {date_end}
        Last Meeting/Conference End Time: {time_end}
        From Destination: {dest_from}
        To Destination: {dest_to}
        Regulations Behavior: {textarea_one}
        
        Additional Information: 
        Additional Travel: {textarea_two}
        Comments: {textarea_three}
        '''
    }

def group_data(email_subject, email_message, email_type):
    send_mail(
        email_subject, 
        email_message, 
        config('EMAIL_HOST_USER'), 
        [email_type] # Approver 1 or 2
    )

# def get_approver(email_type):
    # pass

def send_message(request):
    if request.method == 'GET':
        return render(request, 'main.html')
    elif request.method == 'POST':
        email_type = request.POST.get('button')
        
        if email_type in ('Business', 'Business and Personal'):
            # approver = get_approver(email_type)
            user_email = request.user.username if request.user.is_authenticated else redirect('authentication') 
            if user_email:
                email_data = build_message(request)
                group_data(
                    email_data['email_subject'],
                    email_data['email_message'],
                    # approver_email,
                )
            return redirect('main')
            