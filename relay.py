##########    Relay board switching     ##########


# Import required libraries
from gpiozero import *
from time import sleep
import os

# Hold & repeat variables
hold = 2
repeat = 3

# Clear the screen
os.system('clear')

def relay():
	# Set object relay to a digital device on pin 17
	relay = DigitalOutputDevice(17)
	# Switch object relay ON
	relay.on()
	# Debugging
	print "ON"
	# Wait for hold seconds
	sleep(hold)
	# Switch object relay OFF
	relay.off()
	# Debugging
	print "OFF"
	# Close object relay & release resources **** GOOD HOUSEKEEPING ****
	relay.close()


# Run the demo in a loop
for i in range(0,repeat):
	relay()
	sleep(hold)

