print("\n*****************************************************\n")  # Print a decorative line to separate output

print("Gasoline Branch")  # Print a label for the gasoline-related functionality

import random  # Import the random module for random selection
from time import sleep  # Import the sleep function to simulate delays


# Function to randomly select a gas level from a predefined list
def GasLevelGauge():
    GasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(GasLevelList)  # Return a random gas level


# Function to randomly select a gas station from a predefined list
def GasStations():
    GasStationList = ["BP", "Shell", "Meijer", "Marathon", "Circle K", "Speedway", "Mobile", "Sams Club"]
    return random.choice(GasStationList)  # Return a random gas station


# Function to simulate gas level alerts based on the current gas level
def GasLevelAlert():
    # Randomly generate distances to the closest gas station
    MilesToGasStationLow = round(random.uniform(1, 25), 1)  # Distance for "Low" gas level
    MilesToGasStationQuarter = round(random.uniform(25.1, 50), 1)  # Distance for "Quarter Tank" gas level
    GasLevelIndicator = GasLevelGauge()  # Get the current gas level using GasLevelGauge

    # Check the gas level and print corresponding messages
    if GasLevelIndicator == "Empty":  # If gas tank is empty
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2)  # Simulate a delay
        print("Calling Triple AAA")  # Indicate that the user is calling for roadside assistance
    elif GasLevelIndicator == "Low":  # If gas tank is low
        print("Your gas tank is extremely low, checking GPS for the closest gas station...")
        sleep(3)  # Simulate a delay
        print("The closest gas station is;", GasStations(), "which is", MilesToGasStationLow, "miles away")
    elif GasLevelIndicator == "Quarter Tank":  # If gas tank is a quarter full
        print("Your gas tank is on a quarter of a tank, checking GPS for the closest gas station...")
        sleep(3)  # Simulate a delay
        print("The closest gas station is;", GasStations(), "which is", MilesToGasStationQuarter, "miles away")
    elif GasLevelIndicator == "Half Tank":  # If gas tank is half full
        print("Your gas tank is half a tank full")
    elif GasLevelIndicator == "Three Quarter Tank":  # If gas tank is three-quarters full
        print("Your gas tank is three quarters of a tank full")
    else:  # If gas tank is full
        print("Your gas tank is full")


GasLevelAlert()  # Call the GasLevelAlert function to display the gas status and alert
