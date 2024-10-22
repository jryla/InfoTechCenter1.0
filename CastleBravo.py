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

print("\n*****************************************************\n")
print("Gasoline Branch")
GasLevelAlert()  # Call the optimized alert function
