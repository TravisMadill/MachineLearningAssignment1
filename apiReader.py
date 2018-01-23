import pandas as pd
import requests

url = 'https://www.metaweather.com/api/location/44418/'

response = requests.get(url)
while response.status_code != 200:
	response = requests.get(url)

headers = ['id', 'weather_state_name', 'weather_state_abbr', 'wind_direction_compass', 'created', 'applicable_date', 'min_temp', 'max_temp', 'the_temp', 'wind_speed', 'wind_direction', 'air_pressure', 'humidity', 'visibility', 'predictability']
data = response.json()['consolidated_weather']
data = pd.DataFrame(data, columns=headers)

data.to_csv('london_weather.csv', index=False)