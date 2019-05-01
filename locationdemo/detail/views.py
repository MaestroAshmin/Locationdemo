from django.shortcuts import render, redirect
from .models import Detail
from geopy.geocoders import Nominatim
from django.contrib import messages


def form(request):
    return render(request, 'detail/form.html')


def add_detail(request):
    name = request.POST['college_name']
    street = request.POST['Street']
    city = request.POST['City']
    loc = Nominatim(user_agent="Example")
    location = loc.geocode(name)
    info = Detail(name=name, street=street, city=city, longitude=location.longitude, latitude=location.latitude)
    info.save()
    return redirect('form')


