import requests

from datetime import datetime

api_key = '1450166fb227fd59815c3310cc27ea9c'

location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#create a file with the name 'output' , w is a file access mode which means to write only
text = open("output.txt", 'w')

#using file function in print to redirect the program output to the text file
print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time), file=text)
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city), file=text)
print ("Current weather desc  :", weather_desc, file=text)
print ("Current Humidity      :", hmdt, '%', file=text)
print ("Current wind speed    :", wind_spd, 'kmph', file=text)

#closing the text file so no further data will be redirected
text.close()

#Opening the text file and using a file access mode 'r' which means to read only
text = open("output.txt", 'r')

#printing the text file data in the outout terminal
print(text.read())