print("\n*********************************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherforecast = ["snowing", "blizzard", "raining", "windy", "icy", "sunny"]
    weathercondition = random.choice(weatherforecast)
    return weathercondition

print(weather())




