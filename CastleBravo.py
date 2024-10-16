print("\n*********************************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherforecast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    weathercondition = random.choice(weatherforecast)
    return weathercondition

weatherAlert = weather()



# Dictionary to store weather conditions and corresponding delay and speed limit values
weather_conditions = {
   "snowy": (10, 80),      # 30 min delay, 55 MPH speed limit for snowy weather
   "blizzard": (35, 70),   # 45 min delay, 45 MPH speed limit for blizzard
   "rainy": (3, 90),      # 15 min delay, 65 MPH speed limit for rainy weather
   "windy": (3, 100),      # 10 min delay, 70 MPH speed limit for windy conditions
   "icy": (3, 80)         # 50 min delay, 30 MPH speed limit for icy conditions
}

# Function to respond to weather conditions and adjust vehicle response system (VRS)
def vehicleResponseSystem():
   # Get the condition if the weatherAlert exists in the weather_conditions dictionary
   condition = weather_conditions.get(weatherAlert)

   if condition:
       delay, speed_limit = condition  # Unpack the tuple for delay and speed limit
       # Notify the user of the delay due to the weather condition
       print(f"\nThe National Weather Service has Set an Alarm to {delay} Minutes Because"
             f" of the expected {weatherAlert} Weather Conditions.")
       sleep(1)  # Simulate a pause for a more realistic effect
       # Notify the user of the speed limit enforced by the VRS based on the weather
       print(f"\nVRS System Has Been Engaged, Only Allowing {speed_limit}-MPH.")
   else:
       # If the weather condition is not listed (clear skies or unknown condition)
       print(f"\nThe National Weather Service is Calling for {weatherAlert} Weather, Drive Carefully!")
       sleep(1)  # Simulate a pause
       # Notify the user that the VRS has been disengaged
       print("\nVRS System Has Been Disengaged.")


# Call the vehicleResponseSystem function to run the VRS based on the current weather alert
vehicleResponseSystem()


def vehicleRS():
    if weatherAlert == "snowy":
        print("\nThe National Weather service has updated our alarm by 30 minutes \nof the forecast of", weatherAlert, "weather conditions.")

vehicleRS()