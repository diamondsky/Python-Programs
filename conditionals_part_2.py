#conditionals_part_2.py
from sense_hat import SenseHat

def main():
    sense = SenseHat()
    answer = input("Do you want to see the humidity?\n")
    humidity = sense.get_humidity()
    if answer.lower() == "y" or answer.lower() == "yes":
        sense.show_message("The humidity is " +
                           str(humidity), back_colour=(0,0,0),
                           text_colour = (0,0,255), scroll_speed = 0.1)
    answer = input("Are you a member of the club?\n")
    amount_spent = float(input("How much did you spend?\n"))
    if (answer.lower() == "y" or answer.lower() == "yes") and \
    amount_spent > 100:
        discount = 0.10
        cost = amount_spent - discount * amount_spent
    elif amount_spent > 100:
        discount = 0.05
        cost = amount_spent - discount * amount_spent
    else:
        cost = amount_spent
    sense.show_message("Your cost is $" + format(cost,'5.2f'),
                       text_colour = (0,255,0), back_colour =
                       (0,0,0), scroll_speed = 0.1)
main()
