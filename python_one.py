#HW 1 Kiana Slimak
from sense_hat import SenseHat
from time import sleep
from random import randint

def main():
    sense = SenseHat()

    sense.show_message("Kiana",
                        text_colour = (0,255,255),
                        back_colour = (255,255,0), scroll_speed = 0.2)
    sense.clear()

    temperature = sense.get_temperature()
    kelvin = temperature + 273.15
    sense.show_message("Temperature = " + format(kelvin, '8.3f'),
                       text_colour = (0,255,0),
                       back_colour = (0,0,0), scroll_speed = 0.05)
    sense.clear()

    sense.set_pixel(3,1,0,255,255)
    sleep(.3)
    sense.set_pixel(5,1,0,255,255)
    sleep(.3)
    sense.set_pixel(4,3,255,255,0)
    sleep(.3)
    sense.set_pixel(2,4,128,0,200)
    sleep(.3)
    sense.set_pixel(3,5,128,0,200)
    sleep(.3)
    sense.set_pixel(4,5,128,0,200)
    sleep(.3)
    sense.set_pixel(5,5,128,0,200)
    sleep(.3)
    sense.set_pixel(6,4,128,0,200)
    sleep(.3)
    """sleep(3)"""
    sense.clear()

    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    sense.show_letter("K", text_colour = [r,g,b])
    sleep(.4)
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    sense.show_letter("I", text_colour = [r,g,b])
    sleep(.4)
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    sense.show_letter("A", text_colour = [r,g,b])
    sleep(.4)
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    sense.show_letter("N", text_colour = [r,g,b])
    sleep(.4)
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    sense.show_letter("A", text_colour = [r,g,b])
    sleep(.4)
    sense.clear()
main()
