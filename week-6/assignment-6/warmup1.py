def greeting(name, greet = "Hello"):  # Defining the function
  print(f"{greet}, {name}")

greeting("Fred")                      # Calling the fuunction with just the argument

greeting("Fred", "Welcome")           # Calling the fuunction with the argument and a costum greeting

greeting("Fred",  greet = "Welcome")  # Calling the function using a Keyword argument fot the greeting
