#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
try:
        while True:
                GPIO.output(24, True)
                time.sleep(0.4)
                GPIO.output(24, False)
                time.sleep(0.4)

except KeyboardInterrupt:
        pass

GPIO.cleanup()
