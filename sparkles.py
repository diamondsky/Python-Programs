#sparkles.py
from sense_hat import SenseHat
from random import randint
from time import sleep

def main():
    sense = SenseHat()
    try:
        while True:
            x = randint(0,7)
            y = randint(0,7)
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            sense.set_pixel(x,y,r,g,b)
            sleep(0.001)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        sense.clear()
main()
