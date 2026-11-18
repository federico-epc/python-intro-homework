import datetime

today = datetime.datetime.now()
formatted_date = today.strftime("%B %d, %Y")

print(f"Today is {formatted_date}.")