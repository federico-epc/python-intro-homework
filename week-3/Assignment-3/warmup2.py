# Ages
age = int(input("Please enter your age: "))

if age>=0 and age <=12:                 # 0-12 y.o.
  print("You are a child")
elif age>12 and age <=17:               # 13-17 y.o.
  print("You are a teen")
elif age>17 and age <=64:               # 18-64 y.o.
  print("You are an adult")
elif age>64:                            # >64 y.o
  print("You are a senior")
