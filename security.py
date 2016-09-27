#!/usr/bin/env python
# import required modules
from gpiozero import *
from time import sleep
import signal,os

# stops the button service to avoid conflicts
os.system("systemctl stop buttons.service")
os.system("clear")
print("buttons service stopped")

# define all the leds with thier pin number in a variable
led1 = LED(26)
led2 = LED(19)
led3 = LED(13)
led4 = LED(6)
led5 = LED(5)
led6 = LED(22)

# assign lists to the leds so python will accept it and work with them within the sensing part
thing1 = [led1]
thing2 = [led2]
thing3 = [led3]
thing4 = [led4]
thing5 = [led5]
thing6 = [led6]

# define all the buttons with thier pin number in a variable
button1 = Button(24)
button2 = Button(25)
button3 = Button(12)
button4 = Button(16)
button5 = Button(20)
button6 = Button(21)

# defines the variables in advance and sets the required code pattern
code = '*1234'
in_code = '*'
loop = True

# prints program header when run in the console
print("\n <------ Pi Security ------> \n")

# turns all of the leds off
def clear_led():
#	print("  Clear LED")
	led1.off()
	led2.off()
	led3.off()
	led4.off()
	led5.off()
	led6.off()

# turns all of the leds on
def all_led():
#	print("  All LED")
	led1.on()
	led2.on()
	led3.on()
	led4.on()
	led5.on()
	led6.on()


# define the chase program which will be used to identify it is the security program on the button board
def chase(on,off,count):
	clear_led()
	print("  Function Chase")
	# starts a for loop which repeats the code until the variable i is the same as the count
	for i in range(0,count):
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

def smile(on,off,count):
	clear_led()
	print("  Function Smile")
	for i in range(0,count):
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



# runs the chase program that we defined earlier
chase(.2,.2,2)

def b1():
	global in_code
	for thing in thing1:
		thing.toggle()
		sleep(.2)
		thing.toggle()
		in_code = in_code + '1'
	#	test()

def b2():
	global in_code
	for thing in thing2:
		thing.toggle()
		sleep(.2)
		thing.toggle()
		in_code	= in_code + '2'
#		test()

def b3():
	global in_code
	for thing in thing3:
		thing.toggle()
		sleep(.2)
		thing.toggle()
		in_code = in_code + '3'
#		test()

def b4():
	global in_code
	for thing in thing4:
		thing.toggle()
		sleep(.2)
		thing.toggle()
		in_code = in_code + '4'
#		test()

def b5():
	global in_code
	for thing in thing5:
		thing.toggle()
		sleep(.2)
		thing.toggle()
		in_code = in_code + '5'
#		test()

def b6():
	global in_code
	for thing in thing6:
		thing.toggle()
		sleep(.2)
		thing.toggle()
		in_code = in_code + '6'

def relay():
	sleep(1)
	relay = DigitalOutputDevice(17)
	relay.on()
	sleep(5)
	relay.off()
	relay.close()


button1.when_pressed = b1
button2.when_pressed = b2
button3.when_pressed = b3
button4.when_pressed = b4
button5.when_pressed = b5
button6.when_pressed = b6

while loop == True:
	codeLen = len(in_code)
	if codeLen >= 5:
		if in_code == code:
			print("Ta Da! Unlocking for 5 seconds")
			relay()
		#  ***  Insert code for unlocking here  (set pin of lock to high)  ***
			all_led()
			sleep(5)
			clear_led()
			#  ***  Insert code for locking here  (set pin of lock to low)  ***
			loop = False
		else:
			print(" <--- ALARM! ---> \n <--- ALARM! ---> \n <--- ALARM! ---> \n Incorrect code inputed \n <--- ALARM! ---> \n <--- ALARM! ---> \n <--- ALARM! --->")
			smile(.1,.1,5)
			loop = False

# sleeps for five secconds before restarting the buttons service
sleep(5)
os.system("systemctl start buttons.service")
print("buttons service started")

