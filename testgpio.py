#!/bin/bash

# import gpio
# from signal import pause

gpio mode 4 out
gpio mode 5 out

gpio read 4 
gpio read 5

echo
echo
echo
four=(gpio read 4)
five=(gpio read 5)
echo $four
echo $five
echo
echo
echo
gpio write 4 0
gpio write 5 0

gpio read 4
gpio read 5
# pause()

sleep 1
