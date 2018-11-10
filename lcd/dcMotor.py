#!/usr/bin/python

import RPi.GPIO as GPIO
from modules import DCMOTOR, BUTTON
import signal, sys, time

def sigint_handler(signal, frame):
    print ''
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

stop_button = BUTTON(25)    #purple
right_button = BUTTON(12)   #grey
left_button = BUTTON(24)    #yellow
dcmotor = DCMOTOR(20, 21)

print 'press CTRL+C to exit'

speed = 15

while True:
    if stop_button.isPressed():
        print 'stop'
        dcmotor.stop()
        continue
    if right_button.isPressed():
        print 'right'
        dcmotor.startRight(speed)
        continue
    if left_button.isPressed():
        print 'left'
        dcmotor.startLeft(speed)
    
    time.sleep(0.1)

