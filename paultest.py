# Pi Button Hat system

# This is a library of functions for use with the button board by Paul Collins aka morticiaskeeper

# It uses pin/gpio 15(22),29(05),31(06),33(13),35(19),37(26) for LED's & 18(24),22(25),32(12),36(16),38(20),40(21)

# 39 is LED GND, 34 is Button GND


# Import libraries
from gpiozero import LED, Button
from time import sleep
import signal,os


# Assign led's to gpio pins
led1 = LED(26)
led2 = LED(19)
led3 = LED(13)
led4 = LED(6)
led5 = LED(5)
led6 = LED(22)

# Assign lists to led's
thing1 = [led1]
thing2 = [led2]
thing3 = [led3]
thing4 = [led4]
thing5 = [led5]
thing6 = [led6]

# Assign buttons to gpio pins
button1 = Button(24)
button2 = Button(25)
button3 = Button(12)
button4 = Button(16)
button5 = Button(20)
button6 = Button(21)

# Print program header
print(" ")
print("  Pi Button")
print(" ")


# Define functions

###################################################
############## LED Display Functions ##############
###################################################

# Arguments
# on = time led is on
# off = time led is off
# count = number of iterations

# Demo mode
def demo(on,off,count):
#	green_flash(20,off,20)
	sleep(1)
	yellow_flash(on,off,count)
	sleep(1)
	red_flash(on,off,count)
 	sleep(1)
	chase(on,off,count)
	sleep(1)
	rev_chase(on,off,count)
	sleep(1)
	dot(on,off,count)
	sleep(1)
	rev_dot(on,off,count)
	sleep(1)
	h_block(on,off,count)
	sleep(1)
	v_block(on,off,count)
	sleep(1)
	rev_v_block(on,off,count)
	sleep(1)
	rotate(on,off,count)
	sleep(1)
	rev_rotate(on,off,count)
	sleep(1)
	smile(on,off,count)
	sleep(1)
	blink_all(on,off,count)
	sleep(3)
	all_led()
	sleep(4)
	clear_led()

# Dot
def dot(on,off,count):
	all_led()
	print("  Dot")
	for i in range(0,count):
#		detect()
		led1.off()
		sleep(off)
		led1.on()
		led2.off()
		sleep(off)
		led2.on()
		led3.off()
		sleep(off)
		led3.on()
		led4.off()
		sleep(off)
		led4.on()
		led5.off()
		sleep(off)
		led5.on()
		led6.off()
		sleep(off)
		led6.on()

# reverse dot
def rev_dot(on,off,count):
	all_led()
	print("  Reverse Dot")
	for i in range(0,count):
#		detect()
		led6.off()
		sleep(off)
		led6.on()
		led5.off()
		sleep(off)
		led5.on()
		led4.off()
		sleep(off)
		led4.on()
		led3.off()
		sleep(off)
		led3.on()
		led2.off()
		sleep(off)
		led2.on()
		sleep(off)
		led1.off()
		sleep(off)
		led1.on()

	
# Flash RED
def red_flash(on,off,count):
	clear_led()
	print("  Flash RED")
#	detect()
	led3.blink(on,off,count)
	led6.blink(on,off,count)

# Flash GREEN
def green_flash(on,off,count):
	clear_led()
	print("  Flash GREEN")
	for i in range(0,20):
		if button1.is_pressed:
			print("a")
			detect()
		led1.on()
		led4.on()
		sleep(1)
		led1.off()
		led4.off()
		sleep(1)
	
#	led1.blink(20,20,20)
#	led4.blink(20,20,20)
	
# flash YELLOW
def yellow_flash(on,off,count):
	clear_led()
	print("  Flash YELLOW")
#	detect()
	led2.blink(on,off,count)
	led5.blink(on,off,count)

# All leds ON
def all_led():
#	print("  All LED")
#	detect()
	led1.on()
	led2.on()
	led3.on()
	led4.on()
	led5.on()
	led6.on()

# All leds OFF
def clear_led():
#	print("  Clear LED")
#	detect()
	led1.off()
	led2.off()
	led3.off()
	led4.off()
	led5.off()
	led6.off()

# chase leds
def chase(on,off,count):
	clear_led()
	print("  Chase")
	for i in range(0,count):
#		detect()
		led1.on()
		sleep(off)
		clear_led()		
		led2.on()
		sleep(off)
		clear_led()
		led3.on()
		sleep(off)
		clear_led()
		led6.on()
		sleep(off)
		clear_led()
		led5.on()
		sleep(off)
		clear_led()
		led4.on()
		sleep(off)
		clear_led()

# Smile face
def smile(on,off,count):
	clear_led()
	print(" Smile")
	for i in range(0,count):
#		detect()
		led1.on()
		led3.on()
		led5.on()
		sleep(on)
		led1.off()
		led3.off()
		led5.off()
		led4.on()
		led6.on()
		led2.on()
		sleep(on)
		led4.off()
		led6.off()
		led2.off()

# Reverse chase leds
def rev_chase(on,off,count):
	clear_led()
	print("  Reverse Chase")
	for i in range(0,count):
#		detect()
		led4.on()
		sleep(off)
		clear_led()
		led5.on()
		sleep(off)
		clear_led()
		led6.on()
		sleep(off)
		clear_led()
		led3.on()
		sleep(off)
		clear_led()
		led2.on()
		sleep(off)
		clear_led()
		led1.on()
		sleep(off)
		clear_led()

# blink all the leds
def blink_all(on,off,count):
	clear_led()
	print("  Blink All")
#	detect()
	led1.blink(on,off,count)
	led2.blink(on,off,count)
	led3.blink(on,off,count)
	led4.blink(on,off,count)
	led5.blink(on,off,count)
	led6.blink(on,off,count)

# rotate leds
def rotate(on,off,count):
	clear_led()
	print("  Rotate")
	for i in range(0,count):
#		detect()
		led1.on()
		led6.on()
		sleep(off)
		led1.off()
		led6.off()
		led2.on()
		led5.on()
		sleep(off)
		led2.off()
		led5.off()
		led3.on()
		led4.on()
		sleep(off)
		led3.off()
		led4.off()

# reverse rotate leds
def rev_rotate(on,off,count):
	clear_led()
	print("  Reverse Rotate")
	for i in range(0,count):	
#		detect()
		led1.on()
		led6.on()
		sleep(off)
		led1.off()
		led6.off()
		led3.on()
		led4.on()
		sleep(off)
		led3.off()
		led4.off()
		led2.on()
		led5.on()
		sleep(off)
		led2.off()
		led5.off()

# horizontal block
def h_block(on,off,count):
	clear_led()
	print("  Horizontal blocks")
	for i in range(0,count):
#		detect()
		led1.on()
		led2.on()
		led3.on()
		sleep(off)
		led1.off()
		led2.off()
		led3.off()
		led4.on()
		led5.on()
		led6.on()
		sleep(off)
		led4.off()
		led5.off()
		led6.off()
		sleep(off)

# vertical block
def v_block(on,off,count):
	clear_led()
	print("  Vertical blocks")
	for i in range(0,count):
#		detect()
		led1.on()
		led4.on()
		sleep(off)
		led1.off()
		led4.off()
		led2.on()
		led5.on()
		sleep(off)
		led2.off()
		led5.off()
		led3.on()
		led6.on()
		sleep(off)
		led3.off()
		led6.off()

# Reverse vertical block
def rev_v_block(on,off,count):
	clear_led()
	print("  Reverse Vertical")
	for i in range(0,count):
#		detect()
		led3.on()
		led6.on()
		sleep(off)
		led3.off()
		led6.off()
		led2.on()
		led5.on()
		sleep(off)
		led2.off()
		led5.off()
		led1.on()
		led4.on()
		sleep(off)
		led1.off()
		led4.off()	

###################################################
##############          END          ##############
###################################################



###################################################
################  Button functions ################
###################################################

def thing1_on():
	for thing in thing1:
		thing.toggle()
		fcntest()
#		reboot()

def thing1_off():
	for thing in thing1:
		thing.off()
		fcntest()

def thing2_on():
	for thing in thing2:
		thing.toggle()
		fcntest()

def thing2_off():
	for thing in thing3:
		thing.off()
		fcntest()

def thing3_on():
	for thing in thing3:
		thing.toggle()
		fcntest()

def thing3_off():
	for thing in thing3:
		thing.off()
		fcntest()

def thing4_on():
	for thing in thing4:
		thing.toggle()
		fcntest()

def thing4_off():
	for thing in thing4:
		thing.off()
		fcntest()

def thing5_on():
	for thing in thing5:
		thing.toggle()
		fcntest()

def thing5_off():
	for thing in thing5:
		thing.off()
		fcntest()

def thing6_on():
	for thing in thing6:
		thing.toggle()
		fcntest()

###################################################
##############          END          ##############
###################################################




###################################################
##############       Processes       ##############
###################################################

def reboot():
	yellow_flash(.2,.2,10)
	os.system("reboot")

def shutdown():
	red_flash(.2,.2,10)
	os.system("shutdown -r now /r")

###################################################
##############          END          ##############
###################################################




def fcntest():

# Display LED status to the command line

	A = "OFF"
	B = "OFF"
	C = "OFF"
	D = "OFF"
	E = "OFF"
	F = "OFF"

	os.system("clear")

	print(" ")
	if led6.is_lit == True:
		F = "ON "
	elif led6.is_lit == False:
		F = "OFF"
	if led5.is_lit == True:
		E = "ON "
        elif led5.is_lit == False:
		E = "OFF"
	if led4.is_lit == True:
		D = "ON "
        elif led4.is_lit == False:
		D = "OFF"
	if led3.is_lit == True:
		C = "ON "
        elif led3.is_lit == False:
		C = "OFF"
	if led2.is_lit == True:
		B = "ON "
        elif led2.is_lit == False:
		B = "OFF"
	if led1.is_lit == True:
		A = "ON "
        elif led1.is_lit == False:
		A = "OFF"

	print(" ")
	print(" ")
	print(" **************************")
	print("        LED STATUS")
	print(" **************************")
	print(" ")
	print(" --------------------------")
	print("   |  1   |  2   |  3   |")
	print(" --------------------------")

	print("   | " + A + "  | " + B + "  | " + C + "  |")
	print(" ")
	print(" --------------------------")
	print("   |  4   |  5   |  6   |")
	print(" --------------------------")
	print("   | " + D + "  | " + E + "  | " + F + "  |")
	print(" ")
	print(" **************************")
	print(" **************************")

# Button detection
def detect():
	button1.when_pressed = thing1_on
	button2.when_pressed = thing2_on
	button3.when_pressed = thing3_on
	button4.when_pressed = thing4_on
	button5.when_pressed = thing5_on
	button6.when_pressed = thing6_on
	signal.pause()

###################################################
##############          MAIN         ##############
###################################################

# Run LED demo
while True:
	green_flash(20,20,20)
#	demo(.2,.2,5)
#	detect()

# Detect button presses and call functions

#button1.when_pressed = thing1_on
#button2.when_pressed = thing2_on
#button3.when_pressed = thing3_on
#button4.when_pressed = thing4_on
#button5.when_pressed = thing5_on
#button6.when_pressed = thing6_on


# Keep going until ctrl-C
signal.pause()
print("a")
