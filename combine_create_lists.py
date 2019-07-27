# combine_create_lists.py
# 16 MAR 2018 

def main():
    city_list = ['Lake Worth', 'Austin', 'Los Angelos',]
    state_list = ['Florida', 'Texas', 'California']

    combined_list = city_list + state_list
    i = 0
    while i < len(combined_list):
        print("List value is " + combined_list[i])
        i += 1

    even_list = list(range(0, 20, 2))
    second_list = list(range(3, 35, 4))
    for i in range(0, len(even_list)):
        print(even_list[i])
    for i in range(0, len(second_list)):
        print(second_list[i])
    print(even_list[2:5])
    sliced_list = even_list[0:4] # elements at indiced 0,1,2,3,4
    for i in range(0,len(sliced_list)):
        print(sliced_list[i])
    print(even_list[:5]) # elements at indices 0,1,2,3,4

    try:
        index = int(input("Enter the index of the element"))
        del(even_list[index])
        print("Delete element")
    except:
        print("The element was not found in the list")
        print(even_list[i])

    try:
        index = int(input("Enter the index of the element:"))
        even_list.remove(even_list[index])
        print("Removed element")
    except:
        print("The element was not found in the list")
    for i in range(0, len(even_list)):
        print(even_list[i])

    city_even_list = city_list + even_list
    print(city_even_list)
    i = 0
    while i < len(city_even_list):
        if isinstance(city_even_list[i],int):
            print(format(city_even_list[i],'3d'))
        elif isinstance(city_even_list[i], str):
            print(city_even_list[i])
        i += 1
    
main()
