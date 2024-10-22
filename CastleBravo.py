print("\n*****************************************************\n")

print("Gasoline Branch")

import random
from time import sleep

def GasLevelGauge():
    GasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(GasLevelList)

def GasStations():
    GasStationList = ["BP", "Shell", "Meijer", "Marathon", "Circle K", "Speedway", "Mobile", "Sams Club"]
    return random.choice(GasStationList)

def GasLevelAlert():
    MilesToGasStationLow = round(random.uniform(1,25),1)
    MilesToGasStationQuarter = round(random.uniform(25.1, 50),1)
    GasLevelIndicator = GasLevelGauge()
    if GasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2)
        print("Calling Triple AAA")
    elif GasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking GPS for the closest gas station...")
        sleep(3)
        print("The closest gas station is;", GasStations(), "which is", MilesToGasStationLow, "miles away")
    elif GasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter of a tank, checking GPS for the closest gas station...")
        sleep(3)
        print("The closest gas station is;", GasStations(), "which is", MilesToGasStationQuarter, "miles away")
    elif GasLevelIndicator == "Half Tank":
        print("Your gas tank is half a tank full")
    elif GasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three quarters of a tank full")
    else:
        print("Your gas tank is full")

GasLevelAlert()