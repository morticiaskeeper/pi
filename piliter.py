#!/usr/bin/env python

from gpiozero import PiLiter

lite = PiLiter()

lite.on()
input()
lite.off()
