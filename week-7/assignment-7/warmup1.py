with open("C:/Users/maort/Desktop/Code-The-Dream/python-intro-homework/week-7/data/notes.txt", 'r') as file:
    for i,line in enumerate(file, start=1):
        print(f"Line {i}: {line.strip()}")
