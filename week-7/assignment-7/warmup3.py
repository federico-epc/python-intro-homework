import os

cwd = os.getcwd()
print(cwd)

if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

path = os.path.join("..", "data", "expenses.csv")
print(path)