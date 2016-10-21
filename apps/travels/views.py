from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Trip, Guest
from ..login_reg.models import User


def travels(request):
    trips = Trip.objects.filter(planner_id=request.session['user'].id)
    travels = Trip.objects.filter(id=request.session['user'].id)

    context = {
        "trips": trips,
        "travels": travels,
    }

    return render(request,'courses/travels.html', context)


def destination(request, trip_id):
    results = Trip.objects.get(pk=trip_id)
    guests = Guest.objects.filter(trip_id=trip_id)
    print guests
    for trip in Trip.objects.all():
        print trip.destination, trip.description, trip.start_date, trip.end_date, trip.planner_id.username, trip.id

    context = {
        "trip": results,
        "guests": guests,
    }

    return render(request, 'courses/destination.html', context)


def new_trip(request):
    return render(request, 'courses/new_trip.html')

def add_trip(request):
    if request.method == "POST":
        new_trip = Trip.objects.validate(request.POST, request.session['user'])
        if new_trip[0]:
            messages.success(request, "Congratulations you've created a new trip!")
            return redirect(reverse('travels:home'))
        else:
            print_messages(new_trip[1])
    return redirect(reverse('travels:new_trip'))

def join_trip(request, trip_id):

    user = request.session['user'].id
    trip = Guest.objects.filter(id=trip_id)
    if user != Trip.objects.get(id=trip_id).planner_id:
        if user not in trip:
            s = Guest()
            s.save()
            Guest.objects.create(user_id=user, trip_id=trip_id)
            return redirect(reverse('travels:home'))
        else:
            messages.error("You are already a part of that trip!")




def print_messages(request, error_list):
    for error, tag in error_list:
        messages.error(request, error, tag)
