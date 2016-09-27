import wiringpi2 as wiringpi
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(4, 1)
wiringpi.pinMode(5, 1)
print 'wiringpi pins 4 and 5 set to outputs'
