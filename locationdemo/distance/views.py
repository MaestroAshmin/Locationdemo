from django.shortcuts import render, redirect
from detail.models import Detail
from geopy.geocoders import Nominatim
from math import sin, cos, sqrt, atan2, radians
from decimal import Decimal


def nearby(request):
    return render(request, 'distance/nearby.html')


def calculate_nearby(request):
    hostel_name = request.POST['hostel_name']
    radius = Decimal(6373.0)
    loc = Nominatim(user_agent="Example")
    location = loc.geocode(hostel_name, timeout=3)
    lon = Decimal(radians(location.longitude))
    lat = Decimal(radians(location.latitude))
    detail_set = Detail.objects.all()
    for detail in detail_set:
        print(detail.latitude, detail.longitude, lon, lat)
        lati = Decimal(radians(detail.latitude-lat))
        longi = Decimal(radians(detail.longitude-lon))
        a = Decimal(sin(lati/2)**2 + cos(radians(detail.latitude))*cos(radians(lat))*sin(longi/2)**2)
        distance = 2*radius*Decimal(atan2(sqrt(a), sqrt(1-a)))
        print(distance)
    return redirect('nearby')

