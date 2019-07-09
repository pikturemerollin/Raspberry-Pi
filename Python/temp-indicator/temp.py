#!/usr/bin/env

#import the GPIO libs, sleep command
import RPi.GPIO as GPIO
import time
import os

#define the GPIO pins, in this example we use board pins 7 and 11 on the RPi 3
ledGreen = 7
ledRed = 11

#define the high mark for CPU temperature
highMark = 135.00

#Setup the pin layout to BOARD, i.e: pin number
GPIO.setmode(GPIO.BOARD)

#Setup each pin for output
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.setup(ledRed, GPIO.OUT)

#GPIO.LOW = ON, GPIO.HIGH = OFF
GPIO.output(ledGreen, GPIO.HIGH)
GPIO.output(ledRed, GPIO.HIGH)

#Convert Celsius to Fahrenheit
def celsiusToFahrenheit(degree):
	degree = float(degree)
	#print ("degree = " + str(degree))
	degree = float(degree) * 1.8 + 32
	return degree

#Get the board temperature
def getTemp():
	vcgen = 'vcgencmd measure_temp'
	temperature = os.popen('vcgencmd measure_temp').read()
	#Slice the output to only return the temperature
	temperature = temperature[5:-3]
	return temperature
	
def checkTemp():
	currentTemp = float(celsiusToFahrenheit(getTemp()))
	
	#Check if we are at or above our high mark temperature, if so light up the RED LED
	if currentTemp >= highMark:
		GPIO.output(ledGreen, GPIO.HIGH)
		GPIO.output(ledRed,GPIO.LOW)
		time.sleep(1)
	#Check if we are at or below our high mark temperature, if so light up the GREEN LED
	elif currentTemp < highMark and currentTemp >= 0:
		GPIO.output(ledRed, GPIO.HIGH)
		GPIO.output(ledGreen,GPIO.LOW)
		time.sleep(1)
	#Something went wrong, turn off both LED's
	else:
		GPIO.output(ledRed, GPIO.HIGH)
		GPIO.output(ledGreen,GPIO.HIGH)		
	

try:
	while True:
		checkTemp()
		
except KeyboardInterrupt:
	print('Program execution interrupted')

finally:
	#clean up the GPIO 
	GPIO.cleanup()
	
