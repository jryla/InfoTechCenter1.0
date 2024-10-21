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

print(GasStations(),GasLevelGauge())
#def GasLevelAlert():
