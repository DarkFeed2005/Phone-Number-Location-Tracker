import phonenumbers
from phonenumbers import geocoder
from test import number
import folium 

key = "eb927c8c90184db5a9db0835499dd54a"  # Replace with your actual OpenCage API key

check_number = phonenumbers.parse(number)  
number_location = geocoder.description_for_number(check_number, "en") 
print(f"Location of the number {number} is: {number_location}") 

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode