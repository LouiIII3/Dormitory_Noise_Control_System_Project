import requests
import json

# API_key = "71a7fd6193ea09d86d2d1cc3c79bb259"
url = "https://api.openweathermap.org/data/2.5/weather?q=New%20York&units=metric&appid=71a7fd6193ea09d86d2d1cc3c79bb259"


res = requests.get(url)
wethaerRes = json.loads(res.text)
def getWeather():
    print(wethaerRes['weather'][0]['id'])
    print(wethaerRes['main']['temp'])
    weatherId = wethaerRes['weather'][0]['id']
    temp = wethaerRes['main']['temp']
    return temp, weatherId

t,w = getWeather()
# getWeather()
