
# Number Cruncher refactored

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


# 1. Function to calculate the minimum
def find_min(numbers):
    Num = numbers[0]

    for i in numbers:
        if i < Num:
            Num = i

    return Num


# 2. Function to calculate the maximum
def find_max(numbers):
    Num = numbers[0]

    for i in numbers:
        if i > Num:
            Num = i

    return Num


# 3. Function to search for a number
def search(numbers, target):

    for i in range(len(numbers)):
        if numbers[i] == target:
            return i

    return -1           # returns none


# 4. Sorting function
def bubble_sort(numbers):   # Definning a bubble function

    Sorted = []

    # Copy the original list
    for i in numbers:
        Sorted.append(i)

    # Bubble sort algorithm
    swap = True

    while swap:
        swap = False

        for j in range(len(Sorted) - 1):
            if Sorted[j] > Sorted[j + 1]:
                Num = Sorted[j]
                Sorted[j] = Sorted[j + 1]
                Sorted[j + 1] = Num
                swap = True

    return Sorted


# 5. Function for the main menu and presentation
def show_menu():

    print("---------------------")
    print("   Number Cruncher   ")
    print("---------------------")

    print("Type:\n\n 1) Min to calculate the minimum value\n 2) Max to calculate the maximum value\n 3) S to search for a number\n 4) St to sort the list\n 5) Q to quit the program\n")

    option = input("Type an option from the menu: ").title()

    return option


# 6. Main function. This is the function that controls the operation of the program
def main():

    while True:

        option = show_menu()

        # Quit option
        if option == "Q":
            print("Good bye!")
            break

        # Minimum
        elif option == "Min":
            print("\nMinimum value:", find_min(numbers))

        # Maximum
        elif option == "Max":
            print("\nMaximum value:", find_max(numbers))

        # Searching routine
        elif option == "S":

            number = int(input("Enter number you want to find: "))

            index = search(numbers, number)

            if index != -1:
                print(f"\nFound at index {index}")
            else:
                print("\nNot found")

        # Sort
        elif option == "St":
            print("\nSorted list:", bubble_sort(numbers))

        # Invalid option
        else:
            print("\nPlease enter a valid option.")


# 7. Call the main function
main()
