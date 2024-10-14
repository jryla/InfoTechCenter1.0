print("\n*********************************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherforecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    weathercondition = random.choice(weatherforecast)
    return weathercondition

weatheralert = weather()

def vehicleRS():
    if weatheralert == "snowy":
        print("\nThe National Weather service has updated our alarm by 30 minutes \nof the forecast of", weatheralert, "weather conditions.")

vehicleRS()