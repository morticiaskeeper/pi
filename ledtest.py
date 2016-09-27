#!usr/bin/env python

import rgblib as LED
from time import sleep

count = 0

while count <100:
	LED.Start()
	LED.Red()
	sleep(1)
	LED.Green()
	sleep(1)
	LED.Blue()
	sleep(1)
	LED.Yellow()
	sleep(1)
	LED.Sky()
	sleep(1)
	LED.White()
	sleep(1)
	LED.Pink()
	sleep(1)
	LED.off()
	count = count+1

