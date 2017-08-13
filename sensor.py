import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

while True:
	input_value = GPIO.input(4)
	print "Input Value (PIN 4):", input_value
	time.sleep(0.1) 
