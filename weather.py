import requests
from pprint import pprint
from os import system

def cuurentWeather():

	system('clear')

	print("\n")
	city = input("Please input your city: ")
	print("\n")

	api_address = 'http://api.openweathermap.org/data/2.5/weather?q=Cambridge,uk&units=metric&appid=76fc0f766470f1888f21609f14b7426e'.format(city)

	res = requests.get(api_address)

	data = res.json()

	temp = data['main']['temp']
	max_temp = data['main']['temp_max']
	min_temp = data['main']['temp_min']
	wind_speed = data['wind']['speed']
	latitude = data['coord']['lat']
	longitude = data['coord']['lon']

	description = data['weather'][0]['description']

	print('Temperature : {}'.format(temp), '*')
	print('Wind Speed : {}'.format(wind_speed), ' m/s')
	print('Maximum Temperature : {}'.format(max_temp), '*')
	print('Minimum Temperature : {}'.format(min_temp), '*')
	print('Latitude : {}'.format(latitude))
	print('Longitude : {}'.format(longitude))
	print('Description : {}'.format(description))

	print('\n')
	print("Press any key to return to the Main Menu")

	goBack = input()
	system('clear')

# pprint(data)

