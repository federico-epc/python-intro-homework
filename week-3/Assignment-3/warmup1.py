# Grade calculator
score = int(input("Please enter your score: "))

if score>=90:                 # Any grade above or equal to 90 gets an A
  print(f"Score: {score}\nGrade: A ")
elif score>=80 and score <90: # Grades between 80 and 89 get a B
  print(f"Score: {score}\nGrade: B ")
elif score>=70 and score <80: # Grades between 70 and 79 get a C
  print(f"Score: {score}\nGrade: C ")
elif score>=60 and score <70: # Grades between 60 and 99 get a D
  print(f"Score: {score}\nGrade: D ")
else:
  print(f"Score: {score}\nGrade: F ")  # Grades below 60 get an F
