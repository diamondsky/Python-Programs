#compute_cost.py

def main():
    try:
        purchased = int(input("Enter the number of items: "))
        cost_each = float(input("Enter the cost: "))
        total  = purchased * cost_each
        print("The total cost is $" + format(total, '5.2f'))
    except ValueError:
        total = 0
        print("A non-numeric value was entered")
    finally:
        print("Exiting...")
main()
