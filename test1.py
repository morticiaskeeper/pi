try:
	##########################################################
	#                                                        #
	# 7SegPi Raspberry Pi Code                               #
	# Shows CPU usage 					 #
	#                                                        #
	# www.MaximumOctopus.com                                 #
	# www.MaximumOctopus.com/electronics/pi7seg.htm          #
	#                                                        #
	# code by Paul A Freshney                                #
	#                                                        #
	# July 22nd 2014                                         #
	#                                                        #
	##########################################################
	
	# 7-segment LED connected to 595 shift register
	# right LED, connected to GPIO26 (pin 37)
	# left LED,  connected to GPIO21 (pin 40)

	import RPi.GPIO as GPIO
	import time
	from pi_stats import *
	
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	
	# set to BCM mode, above, so use GPIO designations
	pinDATA  = 4
	pinCLOCK = 27
	pinLATCH = 17

	pinLED1  = 26
	pinLED2  = 21

#########################
#  1 = 3v3  |  5v0 = 2  #
#  3 = SDA  |  5v0 = 4  #
#  5 = SCL  |  GND = 6  #
#  7 = #4   |  TXD = 8  #
#  9 = GND  |  RXD = 10 #
# 11 = #17  |  #18 = 12 #
# 13 = #27  |  GND = 14 #
# 15 = #22  |  #23 = 16 #
# 17 = 3v3  |  #24 = 18 #
# 19 = MOSI |  GND = 20 #
# 21 = MISO |  #25 = 22 #
# 23 = CLK  |  CE0 = 24 #
# 25 = GND  |  CE1 = 26 #
# 27 = I2C  |  I2C = 28 #
# 29 = #05  |  GND = 30 #
# 31 = #06  |  #12 = 32 #
# 33 = #13  |  GND = 34 #
# 35 = #19  |  #16 = 36 #
# 37 = #26  |  #20 = 38 #
# 39 = GND  |  #21 = 40 #
#########################

	GPIO.setup(pinDATA,  GPIO.OUT)    #DATA  (DS)
	GPIO.setup(pinCLOCK, GPIO.OUT)    #CLOCK (SH_CP)
	GPIO.setup(pinLATCH, GPIO.OUT)    #LATCH (ST_CP)

	GPIO.setup(pinLED1, GPIO.OUT)
	GPIO.setup(pinLED2, GPIO.OUT)

# Set ouputs to OFF
	GPIO.output(pinDATA,  False)
	GPIO.output(pinCLOCK, False)
	GPIO.output(pinLATCH, False)

	GPIO.output(pinLED1, False)
	GPIO.output(pinLED2, False)

##########################################################
#                                                        #
# LED digit data                                         #
#                                                        #
##########################################################

# output order
# dp,d,c,g,b,a,f,e
#
#   a              dp    d
# f   b                c   e
#   g                    g 
# e   c                b   f
#   d    dp              a 

# digits 0 - 9 mirror wire front
#        digits = [0b10010000, 0b11010111, 0b10001001, 0b10000011, 0b11000110, 0b10100010, 0b10100000, 0b10010111, 0b10000000,$

# digits 0 - 9 original
#        digits = [0b10010000, 0b11010111, 0b10100010, 0b10000011, 0b11000101, 0b10001001, 0b10001000, 0b11010011, 0b10000000, 0b10000001]

# digits 0 - 9 mirror wire back
	digits = [0b10010000, 0b11111100, 0b10001001, 0b10101000, 0b11100100, 0b10100010, 0b10000010, 0b11111000, 0b10000000, 0b10100000]

# digits 0 - 9 (for use when the display is upside-down)
#	digits = [0b10010000, 0b11111100, 0b10100010, 0b10101000, 0b11001100, 0b10001001, 0b10000001, 0b10111100, 0b10000000, 0b10001000]

# powers of 2 (2^0 to 2^7)
	powers = [1,2,4,8,16,32,64,128]

##########################################################
#                                                        #
# Definitions                                            #
#                                                        #
##########################################################

	def display(dataa, datab):

		GPIO.output(pinLATCH,False)

	#send bits MSB first
		for push in range (0, 8):
	
			GPIO.output(pinDATA, dataa & powers[push])
			GPIO.output(pinCLOCK, True)
			GPIO.output(pinCLOCK, False)
		
		for push in range (0, 8):
	
			GPIO.output(pinDATA, datab & powers[push])
			GPIO.output(pinCLOCK, True)
			GPIO.output(pinCLOCK, False)		

		GPIO.output(pinLATCH,True)
	
		return(0)

##########################################################
##########################################################

	def clearLEDs():

		GPIO.output(pinLATCH, False)

		for push in range (0, 8):
	
			GPIO.output(pinDATA, 255)
			GPIO.output(pinCLOCK, True)
			GPIO.output(pinCLOCK, False)

		GPIO.output(pinLATCH,True)

		return(0)

##########################################################
#                                                        #
# Main Code                                              #
#                                                        #
##########################################################

#	clearLEDs()

	dataIndexa = 0
	dataIndexb = 0

#stats = PiStats()
#stats.update_stats()

##########################################################
##########################################################
	num=13
#	while True:

#		num=0
	
#	if cpu_temp > 99:
#	
#		cpu_temp = 99
		
	dataIndexa = digits[int((num / 10) % 10)]
	dataIndexb = digits[int(num % 10)]
	print(num)
	display(dataIndexa, dataIndexb)
	num = num + 1
	#	print(num)
	time.sleep(.5);
#	stats.update_stats()
except:
	print('ERROR')
#	clearLEDs()	
	GPIO.cleanup()    

##########################################################
##########################################################
