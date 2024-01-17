import phonenumbers
from ph_numbers import number, key
from phonenumbers import geocoder, carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, 'en')
print(location)

service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, 'en'))

geocoder=OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat, lng)


mayMap=folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(mayMap)
mayMap.save('myLocation.html')