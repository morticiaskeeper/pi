#!/usr/bin/env python

# port numbers
from time import sleep
import wiringpi2 as wiringpi

wiringpi.wiringPiSetup()
wiringpi.pinMode(4, 1) # sets wp pin 4 to output
wiringpi.pinMode(5, 1) # sets wp pin 5 to output

#sets both pins to false
wiringpi.digitalWrite(4, 0)
wiringpi.digitalWrite(5, 0)

# read pin state
my_input = wiringpi.digitalRead(4)
five = wiringpi.digitalRead(5)
print my_input
print five


# wait
sleep(5)

# set pin state
wiringpi.digitalWrite(4, 1) # pin 4 to true
wiringpi.digitalWrite(5, 1) # pin 5 to true

# read pin state
four = wiringpi.digitalRead(4)
five = wiringpi.digitalRead(5)
print four
print five

# wait
sleep(5)

# set pin state
wiringpi.digitalWrite(4, 0) # pin 4 to false
wiringpi.digitalWrite(5, 0) # pin 5 to false

# read pin state
four = wiringpi.digitalRead(4)
five = wiringpi.digitalRead(5)
print four
print five

# wait
sleep(20)
print "back to inputs"

#converts back to inputs
wiringpi.pinMode(4, 0)
wiringpi.pinMode(5, 0)

# end

