import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(11, GPIO.IN)
count=0

while True:
    mybutton = GPIO.input(11)
    if mybutton == False:
        count=count+1
        print "count",count
        time.sleep(.5)
