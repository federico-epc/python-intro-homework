num = float(input("Please enter a number: "))

# Check if a number is zero, even, or odd
if num % 2 == 0:
    print(f"\n{num} is even")
else:
    print(f"\n{num} is odd")

# Check whether the number is positive, negative, or zero
if num < 0:
    print(f"{num} is negative")
elif num > 0:
    print(f"{num} is positive")
else:
    print(f"{num} is zero")
