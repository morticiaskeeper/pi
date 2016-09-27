# import functions needed
from time import sleep
import RPi.GPIO as GPIO

# define pin to in or out
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)

# define the button capture function
def capture(time):
     if GPIO.input(11): # if button 11, add 1 to time
          time = (time + 1)
          print(time)

     if GPIO.input(12): # if button 12, take 1 from time
          time = (time - 1)
          print(time)

# set time
time = 1
while 1:
     GPIO.output(13, False) # turn GREEN on
     capture(time) # call capture function
     sleep(time) # wait 
     capture(time) # call capture function
        
     GPIO.output(13, True) # turn GREEN off
     capture(time) # call capture function
     sleep(time) #wait
     capture(time) # call capture function
        
     GPIO.output(15, False) # turn YELLOW on
     capture(time) # call capture function
     sleep(time) # wait
     capture(time) # call capture function
        
     GPIO.output(15, True) # turn YELLOW off
     capture(time) # call capture function
     sleep(time) # wait
     capture(time) # call capture function

     GPIO.output(16, False) # turn RED on
     capture(time) # call capture function
     sleep(time) # wait
     capture(time) # call capture function
        
     GPIO.output(16, True) # turn RED off
     capture(time) # call capture function
     sleep(time) # wait
     capture(time) # call capture function

