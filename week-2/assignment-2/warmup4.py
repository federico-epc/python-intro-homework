# Script with intentional error:
# var1 = "I have "
# var2 = 2
# var3 = " corgis!"
# phrase = var1+var2+var2
# print(phrase)

# 1) 
           ### Error message ###
# File "C:\Users\maort\Desktop\Code-The-Dream\python-intro-homework\week-2\assignment-2\warmup4.py", line 5, in <module>
# phrase =  var1+var2+var3
#              ~~~~^~~~~
# TypeError: can only concatenate str (not "int") to str
#
#2)
              ### What caused it? ### 
# This error ocurred because I was concatenating two different variable types str (var1 and var3)  and int (var2)

# 3)  
              ### How I fixed it ### 

# Define var2 as a str: var2 = "2".

               ## Working script ###
var1 = "I have "
var2 = "2 "
var3 = "Corgis!"
phrase = var1+var2+var3
print(phrase)
phrase =  var1+var2+var3
