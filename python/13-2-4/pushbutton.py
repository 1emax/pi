#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import random
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(12,GPIO.OUT)

while True:
  if GPIO.input(11)==True:
    GPIO.output(12,True)
    print "True"
  else:
    GPIO.output(12,False)
    print "False"
  time.sleep(.2)

