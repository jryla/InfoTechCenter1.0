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
