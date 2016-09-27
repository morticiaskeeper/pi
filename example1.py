##########################################################
#                                                        #
# 7SegPi Raspberry Pi Code                               #
# Example cycles through digits 0-9 on both displays     #
#                                                        #
# www.MaximumOctopus.com                                 #
# www.MaximumOctopus.com/electronics/pi7seg.htm          #
#                                                        #
# code by Paul A Freshney                                #
#                                                        #
# July 31st 2014                                         #
#                                                        #
##########################################################

# 7-segment LED connected to 595 shift register
# right LED, connected to GPIO26 (pin 37)
# left LED,  connected to GPIO21 (pin 40)

import random
import RPi.GPIO as GPIO
import time

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
# 13 = #21  |  GND = 14 #
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

GPIO.output(pinLED1, True)
GPIO.output(pinLED2, True)

dataIndex = 0

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

# digits 0 - 9
#digits = [0b10010000, 0b11010111, 0b10100010, 0b10000011, 0b11000101, 0b10001001, 0b10001000, 0b11010011, 0b10000000, 0b10000001]

# digits 0 - 9 (for use when the display is upside-down)
digits = [0b10010000, 0b11111100, 0b10100010, 0b10101000, 0b11001100, 0b10001001, 0b10000001, 0b10111100, 0b10000000, 0b10001000]


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

    for push in range (0, 16):
    
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

# global time delay time (1.5 seconds)
t=1.5

clearLEDs()

dataIndex = 0

##########################################################
##########################################################

while True:

    display(digits[dataIndex], digits[dataIndex])
    
    time.sleep(t)
    
    dataIndex += 1
    
    if dataIndex == 10:
    
        dataIndex = 0
    
GPIO.cleanup()    

##########################################################
##########################################################
