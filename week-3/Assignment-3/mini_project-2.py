# Daily planner
day = input("What day is today?: ").upper()                             # Ask the user to enter the day he/she wants

if day not in ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]: # Makes sure the day is a valid 
    print("I am sorry, I didn't .")                             # Message iinforming a wrong day input
    day = input("Please retype what day is today?: ").upper()           # upper() normalizes the input

if day in ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]:     # Trying again

    part = input("What part of the day do you want (morning, afternoon, evening)?").upper() # Asaks for the part of the day

    if part not in ["EVENING", "MORNING", "AFTERNOON"]:                             # Checks that the part of the day entered is valid
        print("I am sorry, I didn't understand what you meant.")                    # Prints a message not understanding user's input
        part = input("Please make sure to correctly type the part of the day that you want: ").upper() # Aaking again for part of the day
# Days and suggestuions
    # Monday
    if day == "MONDAY":                                                             # Makes sure that the loop below with suggestions apply only to the selected day
    #
    # The same block structure was used for yhe other days.
    #
        if part == "EVENING":
            print("\nSuggestion: On a Monday evening you can go for a walk at the park!")
        elif part == "MORNING":
            print("\nSuggestion: This Monday morning you can start your day with a delicious cup of coffee!")
        elif part == "AFTERNOON":
            print("\nSuggestion: After having a delicious lunch you can go to Moge Tee and buy a boba tea!")
        else:
          print("Sorry, that is still not a valid. Please run the planner again!")
    # Tuesday 
    elif day == "TUESDAY":
        if part == "EVENING":
            print("\nSuggestion: Get a light dinner and got to bed before 9:00 pm")
        elif part == "MORNING":
            print("\nSuggestion: Go for a 30-minute run and then you could have a healthy breakfast.")
        elif part == "AFTERNOON":
            print("\nSuggestion: Play with your pet!")
        else:
          print("Sorry, that is still not a valid. Please run the planner again!")    
   # Wednesday 
    elif day == "WEDNESDAY":
        if part == "EVENING":
            print("\nSuggestion: Go playing pool!")
        elif part == "MORNING":
            print("\nSuggestion: Do upper-body exercises!")
        elif part == "AFTERNOON":
            print("\nSuggestion: Have lunch at a mexican resaurant.")
        else:
          print("Sorry, that is still not a valid. Please run the planner again!")
   # Thursday 
    elif day == "THURSDAY":
        if part == "EVENING":
            print("\nSuggestion: Have dinner at Bullock's!")
        elif part == "MORNING":
            print("Wake up early an see if it's possible to watch the sunrise!")
        elif part == "AFTERNOON":
            print("\nSuggestion: Have lunch with co-workers at the cafeteria!")
        else:
          print("Sorry, that is still not a valid. Please run the planner again!")
   # Friday 
    elif day == "FRIDAY":
        if part == "EVENING":
            print("\nSuggestion: Go clubbing!")
        elif part == "MORNING":
            print("\nSuggestion: Breakfast outside and enjoy the morning!")
        elif part == "AFTERNOON":
            print("\nSuggestion: Go for a walk with your friends!")
        else:
          print("Sorry, that is still not a valid. Please run the planner again!")
else:
    print("Sorry, that is still not a valid weekday. Please run the planner again!")