# monitor_temperature.py
# 16 MAR 2018

from sense_hat import SenseHat
from time import sleep

def main():
    sense = SenseHat()
    temp_list = [] # create an empty list
    try:
        index = 0
        while True:
            temp_list.append(sense.get_temperature())
            sleep(1)
    except KeyboardInterrupt:
        print("Monitoring completed")
    for index in range(0, len(temp_list)):
        print(format(temp_list[index], '7.3f'), end = '')
        if index%5 == 0 and index != 0:
            print()
    print()
    min_value = min(temp_list)
    print("Minimum temperature " + \
          format(min_value, '7.3f'))
    max_value = max(temp_list)
    print("Maximum temperature " + \
          format(max_value, '7.3f'))
    average_temp =sum(temp_list)/len(temp_list)
    print("Average temperature " + \
          format(average_temp, '7.2f'))
    temp_list.sort()
    print("Sorted list")
    index = 0
    while index < len(temp_list):
        print(format(temp_list[index], '7.2f'), end = '')
        index = index + 1
        if index %5 == 0: # add a new line every five elements
            print()
    print()
    temp_list.reverse()
    print("Sort list in reverse")
    index = 0
    while index < len(temp_list):
        print(format(temp_list[index], '7.2f'), end = '')
        index = index + 1
        if index % 5 == 0: # add a new line every five elements
            print()
    print()
main()
            
