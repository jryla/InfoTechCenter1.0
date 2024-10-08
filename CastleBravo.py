import sys
import time

print("\nWelcome to InfoTechCenter V1.0")


x = 0
ellipses = 0

while x != 20:
    x += 1
    message = ("InfoTech Center System Booting" + "." * ellipses)
    ellipses += 1
    sys.stdout.write("\r" + message)
    time.sleep(.5)
    if ellipses == 4:
        ellipses = 0
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted\n")
