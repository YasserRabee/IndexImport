import json
import requests
import sys

if len(sys.argv) < 1:
    print('Usage: OpenWeatherMap.py zipcode')
    sys.exit()
location = ' '.join(sys.argv[1:])

aapid='6b917d2932792806ba0594461b835275'

unitsOfMeasure='metric'

url = 'http://api.openweathermap.org/data/2.5/weather?zip=%s,us&units=%s&APPID=%s' % (location,unitsOfMeasure,aapid)
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
print('Current weather location is:', weatherData['name'])
print(weatherData)


