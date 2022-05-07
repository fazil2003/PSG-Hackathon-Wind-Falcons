import urllib.parse
import requests
import json


def get_direction(start=None,end=None,APK='5b3ce3597851110001cf6248ed666aca9f834e11a2f70ec7cb89d31c'):
	# APK='5b3ce3597851110001cf6248ed666aca9f834e11a2f70ec7cb89d31c'
	
	#start='Fun mall, Coimbatore'
	url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(start) +'?format=json'
	response = requests.get(url).json()
	start_lon = response[0]["lon"]
	start_lat = response[0]["lat"]

	#end='Shivaji Nagar, Bangalore, KA 560001'
	url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(end) +'?format=json'
	response = requests.get(url).json()
	end_lon = response[0]["lon"]
	end_lat = response[0]["lat"]

	headers = {
		'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
	}
	loc='https://api.openrouteservice.org/v2/directions/driving-car?api_key='+ APK+ '&start='+ start_lon+','+start_lat+ '&end=' + end_lon+','+end_lat
	call = requests.get(loc, headers=headers)
	result = json.loads(call.text)
	result.update({"start":start.lower(), "end":end.lower()})
	return result
#print(get_direction())