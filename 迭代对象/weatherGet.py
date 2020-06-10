# encoding=utf8
from collections.abc import Iterable, Iterator
import requests

class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        if self.index ==len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)


    def get_weather(self,city):
         url = 'http://wthrcdn.etouch.cn/weather_mini?city=%s'%city
         r = requests.get(url)
         data = r.json()['data']['forecast'][0]
         return city, data['high'], data['low']

class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


def show(w):
    for x in w:
        print(x)

if __name__ == "__main__":
    weather = WeatherIterable(['成都','上海','天津'])
    show(weather)



