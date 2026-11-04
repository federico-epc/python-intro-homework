# Printing positive numbers

while True:
    try:
        number = int(input("Please enter a positive integer: "))

        if number > 0:
            break
        else:
            print(f"{number} is not positive! Try again.")

    except ValueError:
        print("The input is invalid! Please enter an integer.")

print(f"{number} is a positive integer!")
