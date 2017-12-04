import json
import requests
import sys

if len(sys.argv) < 1:
    print('Usage: OpenWeatherMap.py zipcode')
    sys.exit()
location = ' '.join(sys.argv[1:])

aapid='6b917d2932792806ba0594461b835275'

url = 'http://api.openweathermap.org/data/2.5/weather?zip=%s,us&APPID=%s' % (location, aapid)
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
w = weatherData
print(w)

# print('Current weather is %s:' % (location))
# print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
# print()
# print('Tomorrow:')
# print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
# print()
# print('Day after tomorrow:')
# print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])