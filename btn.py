from gpiozero import Button
from signal import pause
from time import sleep

button6 = Button(21)

def show():
	print("Button 6 pressed")


button6.when_pressed = show()

pause()

