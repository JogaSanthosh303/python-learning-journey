# conditional statements / decision making statements

""" if
else
elif
nested if


syntax :

if condition :
    statements
else :
    statements """


if True :
    print(" yes this is if condition ")
elif False:
    print("This is elif condition")
else :
    print ("This is else condition")

# -------------------------------------------------------

if True:
    print ("outer if ")
    if False :
        print("inner if")
    else :
        print("inner else")
else : 
    print("Outer else")

# -----------------------------------------------------

age =18
if age>18 or age ==18 :
    print ("you can vote")
else :
    print ("wait")
