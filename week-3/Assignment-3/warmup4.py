num = float(input("Please enter a number: "))

if num==0:
  print(f"\n{num} is Zero")
elif num%2 == 0:
  print(f"\n{num} is even")
elif num == 0:
  print(f"{num} is zero")
else:
  print(f"\n{num} is odd")

if num*(-1)>0:
  print(f"{num} is negative")
else:
  print(f"{num} is positive")
