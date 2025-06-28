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
geocoder = OpenCageGeocode(key)
query = str(number_location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(f"Latitude: {lat}, Longitude: {lng}")

map_location = folium.Map(location=[lat, lng], zoom_start=10)
folium.Marker([lat, lng], popup=number_location).add_to(map_location)
map_location.save("location_map.html")
print("Map has been saved to location_map.html")