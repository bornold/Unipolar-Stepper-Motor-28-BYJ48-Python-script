#/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

# init list with pin numbers
pins = [17,18,22,23]

fullStepsPerRev = 512

# time to sleep between operations between pin activatio between pin activation
stepSleep = .0015

h = GPIO.HIGH
l = GPIO.LOW

def setup():
    GPIO.setmode(GPIO.BCM)
    # loop through pins and set mode and state to 'low'
    for i in pins: 
        GPIO.setup(i, GPIO.OUT) 
        GPIO.output(i, l)
def cleanup():
    GPIO.cleanup()

fullStep = [[l, h, h, h],
            [l, l, h, h],
            [h, l, h, h],
            [h, l, l, h],
            [h, h, l, h],
            [h, h, l, l],
            [h, h, h, l],
            [l, h, h, l]]

fullStepRev = fullStep[::-1]

def forwardBy(fraction):
    rotateBy(fraction, fullStep)

def backBy(fraction):
    rotateBy(fraction, fullStepRev)

def rotateBy(fraction, steps):
    for _ in range(int(fullStepsPerRev*fraction)):
        for step in steps:
            activate(step)
            sleep(stepSleep)

def forwardFor(seconds):   
    activateUntill(fullStep, seconds)

def backFor(seconds):
    activateUntill(fullStepRev, seconds)

def activateUntill(steps, seconds):
    while seconds > 0:
        for step in steps:
            sleep(stepSleep)
            activate(step)
            seconds -= stepSleep

def activate(step):
    for i in range(len(step)):
        GPIO.output(pins[i], step[i])

def forward():
    forwardFor(stepSleep)
def back():
    backFor(stepSleep)

