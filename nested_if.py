#nested_if.py
from sense_hat import SenseHat

def main():
    sense = SenseHat()
    temperature = sense.get_temperature()
    fahrenheit = (temperature + 32)*9/5
    humidity = sense.get_humidity()
    if fahrenheit > 85:
        if humidity > 40:
            sense.show_message("It is hot " + \
                        format(fahrenheit, '7.1f') + \
                        "and humid " + \
                        format(humidity, '6.2f'), scroll_speed = 0.05,
                        text_colour = (255,0,0),
                        back_colour = (0,0,255))
        else: #humidity <= 40
            sense.show_message("It is hot " + \
                        format(fahrenheit, '7.1f') + \
                        " and dry " + \
                        format(humidity, '6.2f'), scroll_speed = 0.05,
                        text_colour = (255,0,0),
                        back_colour = (255,255,0))
    else: #fahrenheit <= 85
        if humidity > 40:
            sense.show_message("It is cooler " + \
                        format(fahrenheit, '7.1f') + \
                        "and humid " + \
                        format(humidity, '6.2f'), scroll_speed = 0.05,
                        text_colour = (255,0,0),
                        back_colour = (0,0,255))
        else: #humidity <= 40
            sense.show_message("It is cooler " + \
                        format(fahrenheit, '7.1f') + \
                        " and dry " + \
                        format(humidity, '6.2f'), scroll_speed = 0.05,
                        text_colour = (255,0,0),
                        back_colour = (255,255,0))
    sense.clear()
main()
                                      
