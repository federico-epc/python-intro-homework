names = ["Joe", "Glenn", "Matthew", "Luke", "Mark", "Alesia", "Lacey",
         "John", "Paul", "Adam", "Ana", "Rebeca", "Stacey", "Laura",
         "Veronica", "Sarah", "Abraham", "Maria", "Fred", "Ada", "Cesar"]

id = input("Enter a name: ").title()
found = False

for i in range(len(names)):
    if id == names[i]:
        print(f"'{names[i]}' is found in position {i} on the list")
        found = True
        break

if found == False:
    print(f"{id} is not on the list!")