import gpiozero as gpio
import time, signal

led1 = gpio.LED(22)
button1 = gpio.Button(24)
led2 = gpio.LED(5)
button2 = gpio.Button(25)
led3 = gpio.LED(6)
button3 = gpio.Button(12)
led4 = gpio.LED(13)
button4 = gpio.Button(16)
led5 = gpio.LED(19)
button5 = gpio.Button(20)
led6 = gpio.LED(26)
button6 = gpio.Button(21)

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
def led6off():
        print("6 off")
        led6.off

button1.when_pressed = led1.on
button1.when_released = led1.off
button2.when_pressed = led2.on
button2.when_released = led2.off
button3.when_pressed = led3.on
button3.when_released = led3.off
button4.when_pressed = led4.on
button4.when_released = led4.off
button5.when_pressed = led5.on
button5.when_released = led5.off
button6.when_pressed = led6on()
button6.when_released = led6off()
print("ready")
signal.pause()
