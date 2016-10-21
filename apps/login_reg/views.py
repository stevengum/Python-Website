from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.urls import reverse
from .models import User

def index(request):
    if 'user' in request.session:
        return redirect(reverse('travels:home'))
    return render(request, 'login_reg/index.html')


def register(request):
    if request.method=="POST":
        newuser = User.objects.register(request.POST) ##handles the dictionary known as request.POST!
        if newuser[0]:
            print "True!"
            request.session['user'] = newuser[1]
            # messages.success(request, 'Successfully registered!')
            return redirect(reverse('travels:home'))
        print_messages(request, newuser[1]) ##this will return the list of errors populated inside of the models.py
    return redirect(reverse('user:index'))

def login(request):
    if request.method=="POST":
        newuser = User.objects.validateLogin(request.POST)
        if newuser[0]:
            request.session['user'] = newuser[1]
            return redirect(reverse('travels:home'))
        print_messages(request, newuser[1]) ##this will return the list of errors populated inside of the models.py
    return redirect(reverse('user:index'))

def logout(request):
    del request.session['user']
    return redirect(reverse('user:index'))

def print_messages(request, error_list):
    for error, tag in error_list:
        messages.error(request, error, extra_tags=tag)
