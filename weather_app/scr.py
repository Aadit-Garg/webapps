from requests import get
import json
from datetime import datetime

#import pprint
api = "YOUR_API_HERE"
ip = get('https://api.ipify.org').text
print(f"got IP[{ip}]")

lat = get(f"https://ipapi.co/{ip}/latitude/").text
lon = get(f"https://ipapi.co/{ip}/longitude/").text
#print(float(lat),float(lon))

weather = get(f"http://api.weatherapi.com/v1/current.json?key={api}&q={lat},{lon}")
print(weather.cookies,weather,lat,lon,"\n\n\n")

report = (json.loads(weather.content))
print(report)
a = report["current"]["condition"]["text"]
b = report["current"]["condition"]["icon"]
c = report["current"]["temp_c"]
d = report["current"]["humidity"]
h = report["location"]["name"]
if report["current"]["cloud"] == 0:
    e = "clear"
else:
    e = f'{report["current"]["cloud"]}'
f = report["location"]["localtime"]
f = f[-5:]
g = report["current"]["is_day"]
def get_info():
    return (a,b,c,d,e,f,g,h,ip) 
print(f"Todays whether is {a} with {b}\n")
print("+----{Whether Reports}----+")
print(f"|# Whether   : {a}")
print(f"|# Temprature: {c} C")
print(f"|# Humidity  : {d} %")
print(f"|# Clouds    : {e}")
print("+----------{END}----------+\n")