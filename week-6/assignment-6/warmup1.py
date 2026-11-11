def greet(name, greeting="Hello"):  # Defining the function
    print(f"{greeting}, {name}")

greet("Fred")                       # Calling with only the name

greet("Fred", "Welcome")            # Calling with both arguments

greet("Fred", greeting="Welcome")   # Calling with a keyword argument
