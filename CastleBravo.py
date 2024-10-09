import sys  # Importing sys for controlling output display
import time  # Importing time to introduce delay in output

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
