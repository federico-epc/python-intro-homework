# Warmup 2 
list1=["Math","Physics","Grammar","Economics","Religion"]   # list for the student's subjects
student={'name':"Fred", "grade":"A+","subjects":list1}      # Creating a dictionary with the the information of the student

print(student.get("subjects"),'\n')                         # Printing only the subjects that the student is taking


for key, values in student.items():                         # For loop to print every keys and values in the dictionary
  print(f"{key}:{values},\n")

student["graduated"] = False                              # Adding a new key and a new value to the dictionary
print("\n",student)                                              # Printing the new dictionary
