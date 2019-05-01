
from geopy.geocoders import Nominatim

loc = Nominatim(user_agent="Example")
address = "Shamul Boys Hostel"
location = loc.geocode(address)
print(location)
print(location.latitude, location.longitude)
'''

from math import sin, cos, sqrt, atan2, radians
R = 6373.0

lat1 = radians(27.6897)
lon1 = radians(85.34)
lat2 = radians(27.7063)
lon2 = radians(85.3189)
print(lat1)


dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
print(a)
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Result:", distance)

'''

