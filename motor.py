#/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

# init list with pin numbers
pinList = [17,18,22,23]
pinListReversed = list(reversed(pinList))

stepsPerRev = 2048
stepsPerRev2 = 4096

# time to sleep between operations between pin activatio between pin activation
minDelayPerStep = .002

def setup():
    GPIO.setmode(GPIO.BCM)
    # loop through pins and set mode and state to 'low'
    for i in pinList: 
        GPIO.setup(i, GPIO.OUT) 
        GPIO.output(i, GPIO.LOW)

def cleanup():
    # Reset GPIO settings
    GPIO.cleanup()

def step(i):
    GPIO.output(i, GPIO.HIGH)
    sleep(minDelayPerStep)
    GPIO.output(i, GPIO.LOW)

def stepAllFor(l, s=minDelayPerStep):
    while s > 0:
        for i in l:
            step(i)
            s -= minDelayPerStep


def back(s=minDelayPerStep):
    stepAllFor(pinListReversed, s)

def forward(s=minDelayPerStep):
    stepAllFor(pinList, s)
