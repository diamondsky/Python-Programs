#sense_hat_two.py
from sense_hat import SenseHat
from time import sleep
from random import randint

def main():
    sense = SenseHat()

    temperature = sense.get_temperature()
    if temperature > 40:
        sense.show_message("It is hot!",
                           text_colour = (255,0,0),
                           back_colour = (0,0,0), scroll_speed = 0.05)
    elif temperature >= 25:
        sense.show_message("It is warm.",
                           text_colour = (255,128,0),
                           back_colour = (0,0,0), scroll_speed = 0.05)
    else:
        sense.show_message("It is cool.",
                           text_colour = (0,0,255),
                           back_colour = (0,0,0), scroll_speed = 0.05)
    
    sense.show_message("Welcome!")
    sense.show_message("Welcome to Raspberry Pi",
                       text_colour = (255,0,255),
                       back_colour = (0,0,255), scroll_speed = 0.05)
    sense.clear()
    sense.show_letter("F", (255,0,0), (100,100,100))
    sleep(1)
    sense.show_letter("U", (0,255,0), (100,100,100))
    sleep(1)
    sense.show_letter("N", (0,0,255), (100,100,100))
    sleep(1)
    sense.clear()

    sense.set_pixel(0,0,0,255,255)
    sleep(.5)
    sense.set_pixel(3,3,255,255,0)
    sleep(.5)
    sense.set_pixel(7,7,255,0,255)
    sleep(3)
    sense.clear()

    sense_list = [0]*64
    for i in range(0,64):
        print(i)
        value = (randint(0,255),randint(0,255),randint(0,255))
        sense_list[i]=value
    sense.set_pixels(sense_list)
    sleep(10)
    sense.clear()
    help(sense)
        
main()
