score = int(input("Please enter a number: "))

def is_valid_score(score):
    if score in range(0, 101):
        return True
    else:
        return False

if is_valid_score(score):
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")
