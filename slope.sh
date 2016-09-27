#!/bin/bash
level=0
gpio pwm 1 0
while [ $level -lt 1000 ];
        do
        let level=$level+1
        gpio pwm 1 $level
        sleep 1
        done
echo "all up"
while [ $level -gt 1 ];
        do
        let level=$level-1
        gpio pwm 1 $level
        sleep 1
        done
echo "all down"
