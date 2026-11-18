print(not True and False)      # The operator 'and' gives True only if both statements are True, otherwise it gives False. not True is False. False is False. Consequently, False and False gives False.
print(True or False and False) # The operator 'or' Gives True if at least one of the statements is True. The operator 'and' takes higher precedencethan 'or.Hence, False and False gives False, then True or False gives True.
print(not (5 > 3))             # 5 is greater than 3, so that is statement is a True. Then the 'not' reverses that result. Hence, not True gives False.
print(10 == 10 and 4 != 4)     # 10 is obviously 10, so that is a True. 4 not equal 4 is False. Hence, True and False is False.
print(not False or not True)   # 5) not False is True; not True is False. Hence we have True or False which gives True.
