# Write your code here :-)
import RPi.GPIO as GPIO
from time import sleep

from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Now we setup  the GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial= GPIO.LOW)

# Now we switch it on and off
t = 1

while True:
    GPIO.output(8, GPIO.HIGH)
    sleep(t)
    GPIO.output(8,GPIO.LOW)
    sleep(t)

    camera.start_preview()
    sleep(t)
    camera.stop_preview()

    GPIO.output(10,GPIO.HIGH)
    sleep(t)
    GPIO.output(10,GPIO.LOW)
    sleep(t)