# Counting numbers from 1 to 100 using a for loop

update = 0                                                      # Initialize the variable that is going to sum the numbers
for number in range(101):                                       # For loop goes over all integers in range(101)-1
  update+=number                                                # Carries out the sum
print(f"The sum of all numbers between 1 and 100 is: {update}") # Prints the result
