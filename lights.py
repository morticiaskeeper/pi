# imports the required stuff
import wiringpi2 as wiringpi
from time import sleep

# sets up wiringpi in gpio mode
wiringpi.wiringPiSetup()

# reads current values
r1 = wiringpi.digitalRead(4)
r2 = wiringpi.digitalRead(5)
# prints current values
print r1, r2

# detecting current state and setting required state
if r1 == 0 and r2 == 0:
	# sets r1 to TRUE & r2 to FALSE	** MORNING **
	wiringpi.digitalWrite(4, 1)
        wiringpi.digitalWrite(5, 0)
elif r1 == 1 and r2 == 0:
	# sets r1 to TRUE & r2 to TRUE	** DAYTIME **
        wiringpi.digitalWrite(4, 1)
	wiringpi.digitalWrite(5, 1)
elif r1 == 1 and r2 == 1:
	# sets r1 to FALSE & r2 to TRUE	** EVENING **
	wiringpi.digitalWrite(4, 0)
        wiringpi.digitalWrite(5, 1)
elif r1 == 0 and r2 == 1:
	# sets r1 to FALSE & r2 to FALSE  ** NIGHT **
        wiringpi.digitalWrite(4, 0)
	wiringpi.digitalWrite(5, 0)
# prints an error if there is a problem
else:
	print 'ERROR'

#sleep(10)
# display current state
r1 = wiringpi.digitalRead(4)
r2 = wiringpi.digitalRead(5)
print 'Completed',r1,r2
