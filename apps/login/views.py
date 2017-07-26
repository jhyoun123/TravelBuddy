# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    request.session['status'] = False
    return render(request, 'login/index.html')

def register(request):
    results = User.objects.registerVal(request.POST)
    if results['valid']:
        request.session['name'] = User.objects.filter(username = request.POST['username'])[0].name
        messages.error(request, "Register Successful!")
        return redirect('/')
    else: 
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['valid']:
        request.session['name'] = User.objects.filter(username = request.POST['login_username'])[0].name
        request.session['id'] = User.objects.filter(username = request.POST['login_username'])[0].id
        request.session['status'] = True
        return redirect('/travel')
    else:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')