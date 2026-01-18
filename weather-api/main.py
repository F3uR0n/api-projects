import requests
import json
import pyttsx3

engine = pyttsx3.init()

city = input(" Enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=6569fe6e083e4dba8bc73059230808&q={city}"

r = requests.get(url)

wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

y = (f"The current weather in {city} is {w} degrees")

engine.say(y)
engine.runAndWait()
engine.stop()