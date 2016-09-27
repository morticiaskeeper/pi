from gpiozero import LED, Button
from signal import pause
from time import sleep

led1 = LED(22)
button1 = Button(24)
led2 = LED(5)
button2 = Button(25)
led3 = LED(6)
button3 = Button(12)
led4 = LED(13)
button4 = Button(16)
led5 = LED(19)
button5 = Button(20)
led6 = LED(26)
button6 = Button(21)

def led1on():
	print("1 on")
	led1.on
def led1off():
	print("1 off")
	led1.off
def led2on():
        print("2 on")
        led2.on
def led2off():
        print("2 off")
        led2.off
def led3on():
        print("3 on")
        led3.on
def led3off():
        print("3 off")
        led3.off
def led4on():
        print("4 on")
        led4.on
def led4off():
        print("4 off")
        led4.off
def led5on():
        print("5 on")
        led5.on
def led5off():
        print("5 off")
        led5.off
def led6on():
        print("6 on")
        led6.on
	sleep(1)
def led6off():
        print("6 off")
        led6.off

button1.when_pressed = led1on
button1.when_released = led1off
button2.when_pressed = led2on
button2.when_released = led2off
button3.when_pressed = led3on
button3.when_released = led3off
button4.when_pressed = led4on
button4.when_released = led4off
button5.when_pressed = led5on
button5.when_released = led5off
button6.when_pressed = led6on
button6.when_released = led6off
print("ready")
pause()
