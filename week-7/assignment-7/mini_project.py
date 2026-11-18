
import os
import sys
import csv
import datetime

# Check if expenses.csv exists
if not os.path.exists('../data/expenses.csv'):
    print("Error: expenses.csv not found!")
    sys.exit()

# Reading the CSV file into a list of dictionaries
with open('../data/expenses.csv', 'r') as file:
    reader = csv.DictReader(file)
    expenses = list(reader)

# Converting from strings to floats
for expense in expenses:
    expense['amount'] = float(expense['amount'])

# Filtering expenses belonging to Food
food_expenses = [
    expense for expense in expenses
    if expense['category'] == 'Food'
]

# Calculating the total Food expenses
total = sum(expense['amount'] for expense in food_expenses)

# Generating today's date
today = datetime.datetime.now()
formatted_date = today.strftime("%B %d, %Y")

# Writing the report
with open('food_report.txt', 'w') as report:

    report.write(f"Food Expense Report — generated {formatted_date}\n")

    for expense in food_expenses:
        report.write(f"{expense['date']}: ${expense['amount']:.2f}\n")

    report.write(f"Total: ${total:.2f}\n")

print("Food expense report generated successfully!")
