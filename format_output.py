#format_output.py

def main():
    temperature_str = input("Enter the temperature: ")
    temperature = float(temperature_str)
    count = int(input("Enter the number of students: "))
    print("The temperature is " + str(temperature))
    print("The number of students is " + str(count))
    print("Students = " + format(count, '5d'))
    print("Temperature = " + format(temperature, '7.2f'))
    print("Temperature = " + format(temperature, '5.3e') + \
          " count = " + format(count, '2d'))
    print("The number of students is {0:5d}".format(count))
    print("The number of students is {:5d}".format(count))
    print("Students is {0:5d}, Temperature is {1:7.2f}"\
          .format(count, temperature))
    print("Temperature = {1:5.3f} count = {0:0d}"\
          .format(count,temperature))

main()
