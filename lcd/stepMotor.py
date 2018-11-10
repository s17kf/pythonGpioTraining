#!/usr/bin/python

from modules import STEP_MOTOR
from time import sleep

in1 = 19    #bialy
in2 = 13    #szary
in3 = 6     #fioletowy
in4 = 5     #niebieski

motor = STEP_MOTOR(in1, in2, in3, in4)

print '128 steps left'
motor.setLeft(128)
sleep(3)
print '256 steps left'
motor.setLeft(256)
sleep(3)
print '512 steps left'
motor.setLeft(512)

