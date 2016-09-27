##!/usr/bin/env python

import wiringpi2 as wiringpi
from time import sleep
wait = 1


def start():
	wiringpi.wiringPiSetup()

def mode():
	wiringpi.pinMode(0, 1)
	wiringpi.pinMode(1, 1)
	wiringpi.pinMode(2, 1)
	wiringpi.pinMode(3, 1)
	wiringpi.pinMode(4, 1)
	wiringpi.pinMode(5, 1)
	wiringpi.pinMode(6, 1)
	wiringpi.pinMode(7, 1)

def reset():
	wiringpi.digitalWrite(0, 0)
	wiringpi.digitalWrite(1, 1)
	wiringpi.digitalWrite(2, 0)
	wiringpi.digitalWrite(3, 0)
	wiringpi.digitalWrite(4, 0)
	wiringpi.digitalWrite(5, 0)
	wiringpi.digitalWrite(6, 0)
	wiringpi.digitalWrite(7, 0)
	wiringpi.digitalWrite(9, 0)

def dot():
	reset()
	wiringpi.digitalWrite(0, 1)
	print "DOT"

def zero():
	reset()
	wiringpi.digitalWrite(6, 1)
	wiringpi.digitalWrite(2, 1)
	wiringpi.digitalWrite(3, 1)
	wiringpi.digitalWrite(9, 1)
	wiringpi.digitalWrite(7, 1)
	wiringpi.digitalWrite(5, 1)
	print "ZERO"

def one():
	reset()
	wiringpi.digitalWrite(3, 1)
	wiringpi.digitalWrite(2, 1)
	print "ONE"

def two():
	reset()
	wiringpi.digitalWrite(6, 1)
	wiringpi.digitalWrite(2, 1)
	wiringpi.digitalWrite(4, 1)
	wiringpi.digitalWrite(7, 1)
	wiringpi.digitalWrite(9, 1)
	print "TWO"

def three():
	reset()
	wiringpi.digitalWrite(6, 1)
	wiringpi.digitalWrite(2, 1)
	wiringpi.digitalWrite(3, 1)
	wiringpi.digitalWrite(4, 1)
	wiringpi.digitalWrite(9, 1)
	print "THREE"

def four():
	reset()
	wiringpi.digitalWrite(5, 1)
	wiringpi.digitalWrite(4, 1)
	wiringpi.digitalWrite(2, 1)
	wiringpi.digitalWrite(3, 1)
	print "FOUR"

def five():
	reset()
	wiringpi.digitalWrite(6, 1)
	wiringpi.digitalWrite(5, 1)
	wiringpi.digitalWrite(4, 1)
	wiringpi.digitalWrite(3, 1)
	wiringpi.digitalWrite(9, 1)
	print "FIVE"

def six():
	reset()
	wiringpi.digitalWrite(6, 1)
	wiringpi.digitalWrite(5, 1)
	wiringpi.digitalWrite(7, 1)
	wiringpi.digitalWrite(9, 1)
	wiringpi.digitalWrite(3, 1)
	wiringpi.digitalWrite(4, 1)
	print "SIX"

def seven():
	reset()
	wiringpi.digitalWrite(6, 1)
	wiringpi.digitalWrite(2, 1)
	wiringpi.digitalWrite(3, 1)
	print "SEVEN"

def eight():
	reset()
	wiringpi.digitalWrite(6, 1)
	wiringpi.digitalWrite(2, 1)
	wiringpi.digitalWrite(3, 1)
	wiringpi.digitalWrite(9, 1)
	wiringpi.digitalWrite(7, 1)
	wiringpi.digitalWrite(5, 1)
	wiringpi.digitalWrite(4, 1)
	print "EIGHT"

def nine():
	reset()
	wiringpi.digitalWrite(4, 1)
	wiringpi.digitalWrite(5, 1)
	wiringpi.digitalWrite(6, 1)
	wiringpi.digitalWrite(2, 1)
	wiringpi.digitalWrite(3, 1)
	wiringpi.digitalWrite(4, 1)
	print "NINE"

def main():
	start()
	mode()
	sleep(1)
	zero()
	sleep(wait)
	one()
	sleep(wait)
	two()
	sleep(wait)
	three()
	sleep(wait)
	four()
	sleep(wait)
	five()
	sleep(wait)
	six()
	sleep(wait)
	seven()
	sleep(wait)
	eight()
	sleep(wait)
	nine()
	sleep(wait)
	reset()
	dot()
	sleep(wait)
	reset()

if __name__=='__main__':
        main()


