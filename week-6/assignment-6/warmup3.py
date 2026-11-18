# 1.
def root(a):
   c=a**0.5
#print(c)   


#NameError                                 Traceback (most recent call last)
#/tmp/ipykernel_665/3495527939.py in <cell line: 0>()
#      1 def root(a):
#      2    c=a**0.5
#----> 3 print(c)
#      4 
#      5 

#NameError: name 'c' is not defined

# 2.
def root(a):
   return a**0.5
c = root(4)
print(c)
