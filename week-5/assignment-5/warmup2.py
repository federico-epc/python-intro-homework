# Printing positive numbers
number = int(input("Please enter a positive integer: "))
while number<=0:
     print(f"{number} is not positive! Try again")
     number = int(input("Please enter a number "))
print(f"{number} is a  positive integer!")
