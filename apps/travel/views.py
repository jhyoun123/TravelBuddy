# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Trip
from django.contrib import messages
from ..login.models import User

# Create your views here.
def status(valid, request):
    if not valid:
        messages.error(request, "No hacking! Please log in first")
        return True

def index(request):
    if status(request.session['status'], request):
        return redirect('/')
    exclude = []
    for trip in User.objects.get(id=request.session['id']).others.all():
        exclude.append(trip.id)
    context = {
        "myTrips": Trip.objects.filter(owner = User.objects.get(id = request.session['id'])),
        "otherTrips": Trip.objects.exclude(owner=User.objects.get(id=request.session['id'])).exclude(id__in=exclude),
        "joinTrips": User.objects.get(id=request.session['id']).others.all(),
    }
    return render(request, "travel/index.html", context)

def add_home(request):
    if status(request.session['status'], request):
        return redirect('/')
    return render(request, "travel/add_home.html")

def add(request):
    if status(request.session['status'], request):
        return redirect('/')
    results = Trip.objects.addTrip(request.POST, request)
    if results['valid']:
        return redirect('/travel')
    else:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/travel/add_home')

def view(request, id):
    if status(request.session['status'], request):
        return redirect('/')
    context = {
        "trip": Trip.objects.get(id = id),
        "others": Trip.objects.get(id = id).others.all()
    }
    return render(request, "travel/view.html", context)

def join(request, id):
    if status(request.session['status'], request):
        return redirect('/')
    Trip.objects.get(id = id).others.add(User.objects.get(id = request.session['id']))
    return redirect('/travel')