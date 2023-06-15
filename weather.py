import python_weather
import asyncio
from os import name, system

def clr():
	#windows bleh
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
	#will work for linux, bsd, and mac

clr()

async def getweather():
    city = input('Please enter your nearest large city: ')
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get(city)

        print(weather.current.temperature)

        for forecast in weather.forecasts:
            print(forecast)

            for hourly in forecast.hourly:
                print(f' --> {hourly!r}')

asyncio.run(getweather())
