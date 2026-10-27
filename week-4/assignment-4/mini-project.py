students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

# Highest score
highest = students[5]["score"]                      # Initialize the value of the highest score with one of the students in the list
hscorer = students[5]["name"]                       # Initialize the value of the name of the owner of that score

for student in students:                            # The for loop goes over all students in the list while checking their scores
    if student["score"] > highest:                  # Sets the searching condition by every loop comoaring the value for the score of the students with the value of the previous iteration of the loop
        highest = student["score"]                  # Updates the highest score in that iteration of the loop
        hscorer = student["name"]                   # Updates the name corresponding to that highst score 

print(f"Top scorer: {hscorer} ({highest})")

# Calculating the average
sum = 0                     # Initializes twith zero the sum of scores to be updated in every iteration of the loop
for student in students:    # For loop to iterate over the the full list to extract the score of every student and add it to the values stored in the previous iteratoin
  sum += student["score"]
average = sum/len(students) # calculates the average by dividing the sum of the score by the the total number of scores, given by the length of the number of students (i.e., the length of the list)
print(f"Class average: {average}")



# List all unique subjects
set1 = set()                    # initialize an empty set

for student in students:        # For loop to iterate over all the subjects in the dictonary
  set1.add(student["subject"])  # Update and store subjects in every iteration. Because it is a set, it will ignore repeated values
print(f"Subjects: {set1}")


# List of high scorers above 75
top = []

for student in students:
  if student["score"] > 75:
     top.append(student["name"])
print(f"Top scorers: {top}")
