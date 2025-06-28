import phonenumbers
from phonenumbers import geocoder
from test import number
import folium 

check_number = phonenumbers.parse(number)  
number_location = geocoder.description_for_number(check_number, "en") 
print(f"Location of the number {number} is: {number_location}") 

from phone_numbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

