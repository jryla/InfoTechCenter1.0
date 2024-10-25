import sys
import time

green = "\033[92m"
bold = "\033[1m"
reset_color = "\033[0m"  # ANSI escape code to reset to default color

print(f"{bold}\n\tWelcome to InfoTechCenter v1.0{reset_color}")  # Purple text for the welcome message

x = 0
ellipses = 0

while x != 20:
    x += 1
    message = (f"{green}InfoTech Center System Booting{reset_color}" + f"{green}.{reset_color}" * ellipses)
    ellipses += 1
    sys.stdout.write("\r" + message)
    time.sleep(.5)
    if ellipses == 4:
        ellipses = 0
    if x == 20:
        print(f"\n\n\n{bold}OS Booted Up - Retina Scanned - Access Granted{reset_color}")


print("\n***************************************\n")



print("\nWeather Branch\n")


# Import necessary libraries
import random  # For generating random weather conditions
from time import sleep  # For adding delays (to simulate time passing)


# Function to determine the weather condition
def weather():
    weatherForecast = ["snowy", "blizzard", "rainy", "windy", "icy", "Sunny"]  # List of possible weather conditions
    return random.choice(weatherForecast)  # Return the randomly chosen weather condition


# Call the weather function to get the current weather alert
weatherAlert = weather()


# Define a dictionary for weather responses and speed limits
weather_conditions = {
    "snowy": {"delay": 30, "speed_limit": 65},
    "blizzard": {"delay": 45, "speed_limit": 55},
    "rainy": {"delay": 15, "speed_limit": 75},
    "windy": {"delay": 10, "speed_limit": 80},
    "icy": {"delay": 50, "speed_limit": 50}
}


# Function to respond based on the weather condition
def vehicleResponseSystem():
    # Check if the weather condition is in the dictionary
    if weatherAlert in weather_conditions:
        condition = weather_conditions[weatherAlert]
        print(f"\nThe National Weather Service has updated alarm by {condition['delay']} minutes because"
              f" of the Forecast of {weatherAlert} weather conditions.")
        sleep(1)
        print(f"\nVRS System Has Been Engaged, Only Allowing You to Drive {condition['speed_limit']} MPH.")
    else:
        # Handle clear or unlisted weather conditions
        print(f"\nThe National Weather Service is Calling for {weatherAlert} Skies, Drive Safely")
        sleep(1)
        print("\nVRS System Has Been Disengaged.")

# Call the vehicle response system function to output the appropriate response
vehicleResponseSystem()

print("\n***************************************\n")



print("\nGasoline Branch\n")

import random
from time import sleep

# Function to randomly select a gas level from a predefined list
def GasLevelGauge():
    GasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(GasLevelList)

# Function to randomly select a gas station from a predefined list
def GasStations():
    GasStationList = ["BP", "Shell", "Meijer", "Marathon", "Circle K", "Speedway", "Mobile", "Sams Club"]
    return random.choice(GasStationList)

# Function to display gas level alert based on current gas level
def GasLevelAlert():
    GasLevelIndicator = GasLevelGauge()  # Store the gas level result once
    MilesToGasStation = {
        "Low": round(random.uniform(1, 25), 1),
        "Quarter Tank": round(random.uniform(25.1, 50), 1)
    }  # Generate distances for specific gas levels

    alert_messages = {  # Map gas levels to messages
        "Empty": "***WARNING - YOU ARE ON EMPTY***\nCalling Triple AAA",
        "Low": f"Your gas tank is extremely low. Closest gas station is {GasStations()}, {MilesToGasStation['Low']} miles away.",
        "Quarter Tank": f"Your gas tank is at a quarter. Closest gas station is {GasStations()}, {MilesToGasStation['Quarter Tank']} miles away.",
        "Half Tank": "Your gas tank is half full.",
        "Three Quarter Tank": "Your gas tank is three quarters full.",
        "Full": "Your gas tank is full."
    }

    print(alert_messages[GasLevelIndicator])  # Print the corresponding alert message

    # Only delay for critical messages (empty and low gas)
    if GasLevelIndicator in ["Empty", "Low", "Quarter Tank"]:
        sleep(2 if GasLevelIndicator == "Empty" else 1.5)

GasLevelAlert()  # Call the optimized alert function