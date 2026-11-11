
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

# Number Cruncher

while True:                                 # while True keeps the program running until it is quitted

    print("---------------------")          # Prints the header of the program
    print("   Number Cruncher   ")
    print("---------------------")

    print("Type:\n\n 1) Min to calulate the minimum value\n 2) Max to calculate the maximum value\n 3) S to search for a number\n 4) St to sort the list\n 5) Q to quit the program\n")

    option = input("Type an option from the menu: ").title()      # Asks the user what to do. The .title() makes sure to capitalize the first letter of the input

    # Quit option
    if option == "Q":                       # If user types "q" the program ends
        print("Good bye!")
        break

    # Finding minimum value
    elif option == "Min":     
        Num = numbers[0]

        for i in numbers:                   # The for loop runs over the list of numbers comparing them and keeping the minimum value
            if i < Num:
                Num = i

        print("\nMinimum value:", Num)

    # Finding maximum value
    elif option == "Max":                   # The for loop runs over the list of numbers comparing them and keeping the maximum value
        Num = numbers[0]

        for i in numbers:
            if i > Num:
                Num = i

        print("\nMaximum value:", Num)

    # Finding a value                                                
    elif option == "S":
        number = int(input("Enter number you want to find: "))        # Asks the user for a number to find on the list
        found = False                                                 # variable that changes to True when the search loop finds the number and changes to false when not

        for i in range(len(numbers)):
            if numbers[i] == number:
                print(f"\nNumber {number} is located at position {i} on the list.")
                found = True

        if found == False:
            print(f"\n{number} is not on the list.")

    # Sorting 
    elif option == "St":
        Sort = []                                   # Empty list to store the sorted values

        for i in numbers:                           # for loop to append values in the new list
            Sort.append(i)

        swap = True                                 # Variable set to True to handle swapping numbers to order them

        while swap:                                 # Swapping routine
            swap = False

            for j in range(len(Sort) - 1):
                if Sort[j] > Sort[j + 1]:
                    Num = Sort[j]
                    Sort[j] = Sort[j + 1]
                    Sort[j + 1] = Num
                    swap = True

        print("\nSorted list:", Sort)              # Prints sorted list

    else:
        print("\nPlease enter a valid option.")    # Message t rerun the program when invalid option is entered
