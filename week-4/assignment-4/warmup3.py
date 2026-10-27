# Warmup3

# Creating lists
list1 = ["Python", "R", "Pearl", "Java", "Fortran", "C", "C++"]      
list2 = ["Python", "C++", "Go!","Julia", "TeX", "Fortran", "SQL"]

# Craeting sets from lists
set1 = set(list1)
set2 = set(list2)

print(set1.union(set2))           # Printing the union of both sets (All elements in both sets that are not repited)
print(set1.intersection(set2))    # Printing the intersection of both sets (Only elements present in both sets)
print(set1.difference(set2))      # Printing the elements present in the first set but not in the second.
