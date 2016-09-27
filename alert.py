#!usr/bin/env python


# IFTT script to send an email alert

import glob
import time
import urllib, urllib2
from time import sleep
import rgblib as RGB

# define test variables

test = 1
temp = 30.47

# define variables

MIN_T_BETWEEN_WARNINGS = 60 # minutes
EVENT = 'Temp_alert'
BASE_URL = 'https://maker.ifttt.com/trigger/'
KEY = 'dyF4PUi_Ne6Rn8gE5IV52TqcIEMhwLU23ugTa8fi_r2'

# send an IFTTT event
def send_notification(temp):
	print ("Temperature Warning")
	data = urllib.urlencode({'value1' : str(temp)})
	url = BASE_URL + EVENT + '/with/key/' + KEY
	response = urllib2.urlopen(url=url, data=data)
	print(response.read())
	RGB.Start()
	RGB.Red()

if test ==1:
	send_notification(temp)
	sleep(5)


