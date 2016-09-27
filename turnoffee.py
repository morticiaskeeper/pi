#!/usr/bin/env python
# turnoffee.py: Shuts down Raspberry Pi safely after a button press.
# Author: Lee Smith
# Copyright: Copyright 2015, Lee Smith
# Version: 1.0.0
# Maintainer: Lee Smith
# Status: Production
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

import time, os, sys, argparse
import RPi.GPIO as GPIO
from argparse import RawTextHelpFormatter

ledPin = 17
swPin = 4
ledStatus = True
testMode = 0
delay = 20

def ledToggle(duration):
  global ledStatus,testMode,delay
  j = 0
  while (j < 1):
    if not(testMode == 0):
      if ledStatus: sys.stdout.write('+')
      else: sys.stdout.write('-')
      sys.stdout.flush()
    if not(testMode == 2): GPIO.output(ledPin,ledStatus)
    time.sleep(duration)
    j = j+duration
    ledStatus = not(ledStatus)
  delay -= 1

def main(argv):
  global ledPin,swPin,ledStatus,testMode,delay

  parser=argparse.ArgumentParser(
    description='''Turnoffee-Pi help''',
    epilog='''End''',
    formatter_class=RawTextHelpFormatter)
  parser.add_argument('-t','--test', type=int, default=0, choices=[0,1,2], metavar='MODE', help='test mode. Allowed values are: \n0=do not run in test mode (default)\n1=test GPIO pins but do not perform shutdown\n2=do not test GPIO pins or perform shutdown')
  parser.add_argument('-d','--delay', type=int, default=20, choices=range(1,120), metavar='SECS', help='delay in seconds before shutdown is run.\nAllowed values are between 1 and 120 seconds.\nThe default value is 20.')
  args=parser.parse_args()
  testMode=args.test
  delay=args.delay

  print "...Waiting for button event (shutdown delay is set to ",delay," seconds)"
  if not(testMode == 2):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(swPin,GPIO.IN)
    GPIO.setup(ledPin,GPIO.OUT)
    GPIO.output(ledPin,ledStatus)
    GPIO.wait_for_edge(swPin,GPIO.FALLING)
    GPIO.remove_event_detect(swPin)
  ledStatus = not(ledStatus)
  if not(testMode == 0): cmdstring = "echo \"Simulating shutting down Pi safely in %s seconds\" | wall -n" % (delay)
  else: cmdstring = "echo \"Shutting down Pi safely in %s seconds\" | wall -n" % (delay)
  os.system(cmdstring)

  while (delay > 15): ledToggle(1)
  while (delay > 10): ledToggle(0.5)
  while (delay > 5): ledToggle(0.25)
  while (delay > 0): ledToggle(0.125)

  if not(testMode == 2): GPIO.cleanup()
  if not(testMode == 0): 
    cmdstring = "echo \"Shutdown has been simulated\" | wall -n"
    os.system(cmdstring)
  if (testMode == 0): os.system("sudo shutdown -h now \*\*\*\*\*\* Please wait two minutes before disconnecting power \*\*\*\*\*\*")

if __name__=="__main__":
  main(sys.argv[1:])
