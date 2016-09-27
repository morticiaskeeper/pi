##########################################################
#                                                        #
# 7SegPi Raspberry Pi Code                               #
# Shows CPU usage, CPU temp and memory usage in turn     #
#                                                        #
# www.MaximumOctopus.com                                 #
# www.MaximumOctopus.com/electronics/pi7seg.htm          #
#                                                        #
# code by Paul A Freshney                                #
#                                                        #
# August 1st 2014                                        #
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

GPIO.output(pinLED1, True)
GPIO.output(pinLED2, True)

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
digits = [0b10010000, 0b11010111, 0b10100010, 0b10000011, 0b11000101, 0b10001001, 0b10001000, 0b11010011, 0b10000000, 0b10000001]

# digits 0 - 9 (for use when the display is upside-down)
#digits = [0b10010000, 0b11111100, 0b10100010, 0b10101000, 0b11001100, 0b10001001, 0b10000001, 0b10111100, 0b10000000, 0b10001000]

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

clearLEDs()

dataIndexa  = 0
dataIndexb  = 0

status_mode = 0 # which status to show (0=CPU; 1=MEM; 2=TEMP)

stats = PiStats()
stats.update_stats()

##########################################################
##########################################################

while True:

    if status_mode == 0:

        cpu_info = stats.get_cpu_info()
    
        if cpu_info['percent'] > 99:
    
            cpu_info['percent'] = 99
        
        dataIndexa = digits[(int(cpu_info['percent'] / 10) % 10)]
        dataIndexb = digits[int(cpu_info['percent'] % 10)]

        GPIO.output(pinLED1, True)
        GPIO.output(pinLED2, True)

    elif status_mode == 1:

        meminfo = stats.get_memory_info()
    
        if meminfo['percent'] > 99:
    
            meminfo['percent'] = 99
        
        dataIndexa = digits[int((meminfo['percent'] / 10) % 10)]
        dataIndexb = digits[int(meminfo['percent'] % 10)]

        GPIO.output(pinLED1, True)
        GPIO.output(pinLED2, False)

    elif status_mode == 2:

        cpu_temp = stats.temp_in_c
    
        if cpu_temp > 99:
    
            cpu_temp = 99
        
        dataIndexa = digits[int((cpu_temp / 10) % 10)]
        dataIndexb = digits[int(cpu_temp % 10)]

        GPIO.output(pinLED1, False)
        GPIO.output(pinLED2, True)

    display(dataIndexa, dataIndexb)
    
    time.sleep(5);
    stats.update_stats()

    # move to next mode

    status_mode += 1

    if status_mode == 3:

        status_mode = 0
    
GPIO.cleanup()    

##########################################################
##########################################################
