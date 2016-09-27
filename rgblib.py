#!usr/bin/env python


# to call this library from another script, import rgblib as LED. LED.Red() will ight the Red led.


import wiringpi2 as wiringpi
from time import sleep

def Start():
	wiringpi.wiringPiSetup()
	# set pin number to colours
	global RED, GREEN, BLUE
	RED=0
	GREEN=2
	BLUE=3
	# set pins to output mode
	wiringpi.pinMode(RED, 1)
	wiringpi.pinMode(GREEN, 1)
	wiringpi.pinMode(BLUE, 1)
	# write to colours
	wiringpi.digitalWrite(RED, 0)
	wiringpi.digitalWrite(GREEN, 0)
	wiringpi.digitalWrite(BLUE, 0)

def Red():
	wiringpi.digitalWrite(RED, 1)
	wiringpi.digitalWrite(GREEN, 0)
	wiringpi.digitalWrite(BLUE, 0)
	print "RED"

def Green():
	wiringpi.digitalWrite(RED, 0)
	wiringpi.digitalWrite(GREEN, 1)
	wiringpi.digitalWrite(BLUE, 0)
	print "GREEN"

def Blue():
	wiringpi.digitalWrite(RED, 0)
	wiringpi.digitalWrite(GREEN, 0)
	wiringpi.digitalWrite(BLUE, 1)
	print "BLUE"

def Yellow():
	wiringpi.digitalWrite(RED, 1)
	wiringpi.digitalWrite(GREEN, 1)
	wiringpi.digitalWrite(BLUE, 0)
	print "YELLOW"

def Sky():
	wiringpi.digitalWrite(RED, 0)
	wiringpi.digitalWrite(GREEN, 1)
	wiringpi.digitalWrite(BLUE, 1)
	print "SKY"

def White():
	wiringpi.digitalWrite(RED, 1)
	wiringpi.digitalWrite(GREEN, 1)
	wiringpi.digitalWrite(BLUE, 1)
	print "WHITE"

def Pink():
	wiringpi.digitalWrite(RED, 1)
	wiringpi.digitalWrite(GREEN, 0)
	wiringpi.digitalWrite(BLUE, 1)
	print "PINK"

def off():
	wiringpi.digitalWrite(RED, 0)
	wiringpi.digitalWrite(GREEN, 0)
	wiringpi.digitalWrite(BLUE, 0)
	print "OFF"

# main is a test script that will run if rgblib.py is called from the command line
def main():
	Start()
	Red()
	sleep(2)
	Blue()
	sleep(2)
	Green()
	sleep(2)
	Yellow()
	sleep(2)
	Sky()
	sleep(2)
	White()
	sleep(2)
	Pink()
	sleep(2)
	off()


# if called from the command line, run main, otherwise, accept the calling argument
if __name__=='__main__':
	main()
#END



