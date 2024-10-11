import sys  # Importing sys for controlling output display
import time  # Importing time to introduce delay in output

<<<<<<< HEAD
# ANSI escape codes for green text and bold text
green = "\033[92m"  # Green text color
bold = "\033[1m"  # Bold text
reset_color = "\033[0m"  # ANSI escape code to reset to default color

# Welcome message in bold text
print(f"{bold}\n\tWelcome to InfoTechCenter v1.0{reset_color}")  # Bold text for the welcome message

# Delay time before the system starts "booting"
timeToSleep = 1
time.sleep(timeToSleep)  # Calling the time to sleep library with the variable timeToSleep value

x = 0  # Counter for loop iterations
ellipses = 0  # Counter for the number of dots after "booting"

# Loop to simulate booting up process
while x != 20:
    x += 1  # Increment loop counter
    # Create booting message with increasing number of dots (ellipses)
    message = (f"{green}InfoTech Center System Booting{reset_color}" + f"{green}.{reset_color}" * ellipses)
    ellipses += 1  # Increment the ellipses count
    sys.stdout.write("\r" + message)  # Overwrite the current line with the new message
    time.sleep(.5)  # Pause for 0.5 seconds between each iteration

    # Reset ellipses count after it reaches 4
    if ellipses == 4:
        ellipses = 0

    # After 20 iterations, print the final message
    if x == 20:
        print(f"\n\n\n{bold}OS Booted Up - Retina Scanned - Access Granted{reset_color}")  # Final boot-up message
=======
print("\nWelcome to InfoTechCenter V1.0")  # Printing welcome message

x = 0  # Initializing counter to track iterations
ellipses = 0  # Initializing counter to track the number of dots

# Loop to simulate the system booting process
while x != 20:  # Loop will run until x reaches 20
    x += 1  # Incrementing the iteration counter by 1
    message = ("InfoTech Center System Booting" + "." * ellipses)  # Creating boot message with dots based on 'ellipses' count
    ellipses += 1  # Adding an additional dot for the next iteration
    sys.stdout.write("\r" + message)  # Using '\r' to overwrite the current line with the updated message
    time.sleep(.5)  # Pausing the execution for 0.5 seconds to simulate a loading effect
    if ellipses == 4:  # If the ellipses reach 4 dots, reset it back to 0 to loop the dot animation
        ellipses = 0
    if x == 20:  # When x reaches 20, end the loop
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted\n")  # Final message after the boot simulation is complete
>>>>>>> GitHub/WelcomeScreen
