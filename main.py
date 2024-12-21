import opencage
import phonenumbers 
import folium
from herphone import number

from phonenumbers import geocoder

pepnumbers = phonenumbers.parse(number, "CH")
location = geocoder.description_for_number(pepnumbers, "en")

print(location)

from phonenumbers import carrier

service_provider = phonenumbers.parse(number, "RO")

print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

key = 'bea92383f4e74e4796c63d9eb1983507'

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)

# print(result)
 
lat = result[0]['geometry']['lat']
long = result[0]['geometry']['lng']

print(f'Lat: {lat}, Long: {long}')

map = folium.Map(location=[lat, long], zoom_start=9)

folium.Marker([lat, long], popup=location).add_to(map)

map.save('location.html')

