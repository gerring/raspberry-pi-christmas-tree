# Write your code here :-)
import RPi.GPIO as GPIO
from time import sleep

# Now we setup  the GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


# Now we switch it on and off
t = 0.1
pins = [8, 10, 12, 16, 18, 19, 21, 23, 24, 26]

for pin in pins:
    GPIO.setup(pin, GPIO.OUT, initial= GPIO.LOW)

while True:

    for pin in pins:

        GPIO.output(pin, GPIO.HIGH)
        sleep(t)
        GPIO.output(pin,GPIO.LOW)
        sleep(t)