#new_jersey_tax.py
from sense_hat import SenseHat

def main():
    sense = SenseHat()
    earned = float(input("What did you earn?\n"))
    if earned <= 20000:
        tax = 0.014 * earned
    elif earned <= 35000:
        tax = 0.014*20000 + 0.0175*(earned-20000)
    elif earned <= 50000:
        tax = 0.014*20000 + 0.0175*15000 + (earned-35000)*0.0265
    else:
        tax = 0.014*20000 + 0.0175*15000 + 0.0265*15000 + (earned-50000)*0.05125
    sense.show_message("Your tax is $" + \
                       format(tax,'4.2f'), text_colour = (255,255,0),
                       back_colour = (0,0,0), scroll_speed = 0.2)

main()
