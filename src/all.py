# Write your code here :-)
import RPi.GPIO as GPIO
from time import sleep

# Now we setup  the GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# The numbers of the pinss
pins = [8, 10, 12, 16, 18, 19, 21, 23, 24, 26]

def rightleft(t):
    for pin in pins:
        if pin<=18:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)
    sleep(t)

    for pin in pins:
        if pin>=19:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)
    sleep(t)

def interleaf(t):
    eo = [8,12,18,21,24]
    for pin in pins:
        if pin in eo:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)
    sleep(t)

    for pin in pins:
        if not pin in eo:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)
    sleep(t)

def onebyone(t):
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)
        sleep(t)
        GPIO.output(pin, GPIO.LOW)
        sleep(t)

def main():
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT, initial= GPIO.LOW)

    t = 1
    delta = 0.10157
    while True: # Command key not pressed
        #onebyone(t)
        #rightleft(t)

        t = t-(delta*t)
        print(t)
        #interleaf(t)
        rightleft(t)

if __name__ == "__main__":
    main()