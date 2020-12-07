# Write your code here :-)
import RPi.GPIO as GPIO
from time import sleep
from pi import Pi

# The numbers of the pinss
pins = [8, 10, 12, 16, 18, 19, 21, 23, 24, 26]

def init():
    '''
    Get the pins ready. We are using the pins in
    the array [8, 10, 12, 16, 18, 19, 21, 23, 24, 26]
    which is har coded. here.
    :return:
    '''
    # Now we setup  the GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    for pin in pins:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

def rightleft(t):
    '''
    Alternative the pins one right one left splitting the array in the middle.
    :param t: time to sleep between alternation
    :return:
    '''
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
    '''
    Interleave the pins and switch
    between interleaved states.
    :param t:
    :return:
    '''
    eo = [8,12,18,21,24] # TODO use array slciing rather than hard coding.
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

def onebyone(t, clockwise=True):
    '''
    Switch on the pins one by one.
    :param t:
    :return:
    '''
    lights = pins if clockwise else reversed(pins)
    for pin in lights:
        GPIO.output(pin, GPIO.HIGH)
        sleep(t)
        GPIO.output(pin, GPIO.LOW)
        sleep(t)

def number(value, t):
    '''
    Print a number between 0-10 in leds.
    If value>10 they will all be on.
    :param value: 0-10
    :param t: time to wait in this configuration.
    :return:
    '''
    off()

    index = 0
    for pin in pins:
        if index >= value:
            break
        GPIO.output(pin, GPIO.HIGH)
        index += 1
        sleep(t)

def off():
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)


def gettng_faster(t, delta, function):

    # t = 1
    # delta = 0.10157
    while True:
        #onebyone(t)
        #rightleft(t)

        t = t-(delta*t)
        #interleaf(t)
        rightleft(t)


def main():
    init()
    t = 0.1
    while True:

        # Tell user we are starting
        onebyone(0.1)
        onebyone(0.1, False)
        off()
        sleep(2)

        pi = Pi(10000)
        for c in pi.generator():
            number(c, t)

if __name__ == "__main__":
    main()