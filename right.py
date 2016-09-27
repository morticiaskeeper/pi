from gpiozero import LED
from time import sleep
led1=LED(23)
led2=LED(24)
led1.off()
led2.off()
while True:
	led2.toggle()
	sleep(1)
