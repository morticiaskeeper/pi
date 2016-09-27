############################## Head Up Display GPS Speedometer ##############################
show=False
import serial, os, time
import RPi.GPIO as GPIO
log=open('log.txt','a')
newline='\n'
log.write('--------------------BOOT--------------------')
log.write(newline)
log.close()

# Set the GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
log=open('log.txt','a')
log.write('gpio pin set warning off bcm')
log.write(newline)
log.close()

pinDATA = 4
pinCLOCK = 27
pinLATCH = 17
pinLED1 = 26
pinLED2 = 21
log=open('log.txt','a')
log.write('gpio pin numbers set')
log.write(newline)
log.close()

GPIO.setup(pinDATA, GPIO.OUT)
GPIO.setup(pinCLOCK, GPIO.OUT)
GPIO.setup(pinLATCH, GPIO.OUT)
GPIO.setup(pinLED1, GPIO.OUT)
GPIO.setup(pinLED2, GPIO.OUT)
log=open('log.txt','a')
log.write('gpio pins set to output')
log.write(newline)
log.close()

GPIO.output(pinDATA, False)
GPIO.output(pinCLOCK, False)
GPIO.output(pinLATCH, False)
GPIO.output(pinLED2, False)
GPIO.output(pinLED1, False)
log=open('log.txt','a')
log.write('gpio pins set low')
log.write(newline)
log.close()



def clearLEDs():	# Clear the LED display

    GPIO.output(pinLATCH, False)

    for push in range(0, 8):

        GPIO.output(pinDATA, 255)
        GPIO.output(pinCLOCK, True)
        GPIO.output(pinCLOCK, False)

    GPIO.output(pinLATCH, True)
    log=open('log.txt','a')
    log.write('---Clear LED---')
    log.write(newline)
    log.close()

    return(0)


clearLEDs()	# clear the display
print "running"	# show the program is running
GPIO.output(pinLED1, False)	# turn RED LED off

# Mirror digits wires front
#digits = [0b10010000, 0b11010111, 0b10001001, 0b10000011, 0b11000110, 0b10100010, 0b10100000, 0b10010111, 0b10000000, 0b10000010]

# Mirror digits wires back
digits = [0b10010000, 0b11111100, 0b10001001, 0b10101000, 0b11100100, 0b10100010, 0b10000010, 0b11111000, 0b10000000, 0b10100000]
digits3 = [0b11111111, 0b11111100, 0b10001001, 0b10101000, 0b11100100, 0b10100010, 0b10000010, 0b11111000, 0b10000000, 0b10100000]
log=open('log.txt','a')
log.write('digit codes set')
log.write(newline)
log.close()



# No Fix digits
digits2 = [0b11101111]
log=open('log.txt','a')
log.write('no fix digit code set')
log.write(newline)
log.close()


powers = [1,2,4,8,16,32,64,128]

def display(dataa, datab):	# Display the numbers on the 7 segment displays

    GPIO.output(pinLATCH, False)

    for push in range(0, 8):

	GPIO.output(pinDATA, dataa & powers[push])
	GPIO.output(pinCLOCK, True)
	GPIO.output(pinCLOCK, False)
#	log=open('log.txt','a')
#	log.write('First Display')
#	log.write(newline)
#	log.close()


    for push in range(0, 8):

	GPIO.output(pinDATA, datab & powers[push])
	GPIO.output(pinCLOCK, True)
	GPIO.output(pinCLOCK, False)
#	log=open('log.txt','a')
#	log.write('Seccond Display')
#	log.write(newline)
#	log.close()

    GPIO.output(pinLATCH, True)
    return(0)

def NoDisplay():	# Display the no fix digits on the 7 segment display
    GPIO.output(pinLATCH, False)

    for push in range(0, 8):

	GPIO.output(pinDATA, digits2[0] & powers[push])
	GPIO.output(pinCLOCK, True)
	GPIO.output(pinCLOCK, False)
    GPIO.output(pinLATCH, True)
#	log=open('log.txt','a')
#	log.write('===NO FIX===')
#	log.write(newline)
#	log.close()

    return(0)

NoDisplay()

clearLEDs()

dataIndexa=0
dataIndexb=0
speed=0
log=open('log.txt','a')
log.write('defalt data set')
log.write(newline)
log.close()

firstFixFlag = False # this will go true after the first GPS fix.
firstFixDate = ""

# Set up serial:
ser = serial.Serial(
    port='/dev/ttyACM0',\
    baudrate=4800,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=1)

log=open('log.txt','a')
log.write('Serial Setup')
log.write(newline)
log.close()

#########################
GPIO.output(pinLED1, True)
#########################

# Helper function to take HHMM.SS, Hemisphere and make it decimal:
def degrees_to_decimal(data, hemisphere):
    try:
        decimalPointPosition = data.index('.')
        degrees = float(data[:decimalPointPosition-2])
        minutes = float(data[decimalPointPosition-2:])/60
        output = degrees + minutes
        if hemisphere is 'N' or hemisphere is 'E':
            return output
        if hemisphere is 'S' or hemisphere is 'W':
            return -output
    except:
        return ""

# Helper function to take a $GPRMC sentence, and turn it into a Python dictionary.
# This also calls degrees_to_decimal and stores the decimal values as well.
def parse_GPRMC(data):
    data = data.split(',')
    dict = {
            'fix_time': data[1],
            'validity': data[2],
            'latitude': data[3],
            'latitude_hemisphere' : data[4],
            'longitude' : data[5],
            'longitude_hemisphere' : data[6],
            'speed(Kn)': data[7],
            'true_course': data[8],
            'fix_date': data[9],
            'variation': data[10],
            'variation_e_w' : data[11],
            'checksum' : data[12]
    }
    dict['decimal_latitude'] = degrees_to_decimal(dict['latitude'], dict['latitude_hemisphere'])
    dict['decimal_longitude'] = degrees_to_decimal(dict['longitude'], dict['longitude_hemisphere'])
    log=open('log.txt','a')
    log.write('dictonary made')
    log.write(newline)
    log.close()

    return dict
log=open('log.txt','a')
log.write('parse defined, starting loop')
log.write(newline)
log.close()
# Main program loop:
while True:
#    print 1
    line = ser.readline()
    print line
    log=open('log.txt','a')
    log.write(line)
    log.write(newline)
    log.close()
    if "$GPRMC" in line: # This will exclude other NMEA sentences the GPS unit provides.
        print 2
	gpsData = parse_GPRMC(line) # Turn a GPRMC sentence into a Python dictionary called gpsData
	print gpsData
	#log=open('log.txt','a')
	#log.write(gpsData)
	#log.write(newline)
	#log.close
	print gpsData['validity']
	ts = str(time.localtime())
	log=open('log.txt','a')
	log.write('validity: ' + gpsData['validity'])
	log.write(newline)
	log.write(ts)
	log.write(newline)
	log.close()

        if gpsData['validity'] == "A": # If the sentence shows that there's a fix, then we can log the line
	    print("A")
	    show=True
	    GPIO.output(pinLED1, False)
#            if firstFixFlag is False: # If we haven't found a fix before, then set the filename prefix with GPS date & time.
 #               firstFixDate = gpsData['fix_date'] + "-" + gpsData['fix_time']
  #              firstFixFlag = True
   #         else: # write the data to a simple log file and then the raw data as well:
    #            with open("/home/paul/" + firstFixDate +"-simple-log.txt", "a") as myfile:
     #               myfile.write(gpsData['fix_date'] + "," + gpsData['fix_time'] + "," + str(gpsData['decimal_latitude']) + "," + str(gpsData['decimal_longitude']) +"\n")
      #          with open("/home/paul/" + firstFixDate +"-gprmc-raw-log.txt", "a") as myfile:
       #             myfile.write(line)
	    knt = float(gpsData['speed(Kn)']) # Set knt to GPS speed
	    mph = (knt * 1.15)	# Set mph
	    kmh = (knt * 1.852)	# Set kmh
#	    speed = int(knt)	# Set display speed to knt
	    speed = int(mph)	# Set display speed to mph
#	    speed = int(kmh)	# Set display speed to kmh
	    log=open('log.txt','a')
	    log.write('Speeds knt: ' + str(knt) + " mph: " + str(mph) + " kmh: " + str(kmh))
	    log.write(newline)
	    log.close()

	else:
	    show=False
	    speed=0
	    print("nope")
    if speed > 99:	# Set top speed to 99
	speed = 99
	log=open('log.txt','a')
	log.write('===============SPEED TOP===============')
	log.write(newline)
	log.close()

	
#    if speed < 5:	# Ignore speed below 5
#	speed = 0
    if show == True:
	dataIndexa = digits3[int((speed/10)%10)]
	dataIndexb = digits[int(speed%10)]
	display(dataIndexb, dataIndexa)
    elif show == False:
	NoDisplay()
    else:
	"ERROR!!!"
