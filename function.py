""" 
function--> block of code

 """
def func():                        #function definition
    print("this is a function")    #function body
func()                             # function call


def sum(a,b):
    print("This is the sum : " , a+b)
sum(2,3)
func()

# Types of functions

""" def funct1(a):
    print("This is function" , a)  # TypeError: funct() takes 1 positional argument but 3 were given
funct1(1,3,5) 
"""

#orbitory arguments or parameters
def orbitaryfunct2(*a):
    print("This is function" , a) # This is function (1, 3, 5) given. now result get in tuple format
                                  #  so this is orbitary argument or paramerter
                                  #one variable but can pass mulltiple values
orbitaryfunct2(1,3,5)


# keyword argument
def keywordfunct3(**a):                         # Result:This is the keyword function: {'a': 1, 'b': 2, 'c': 5}
    print("This is the keyword function:" , a)  # here result is in like arguments saved in dictonary
keywordfunct3(a=1, b=2 ,c=5)                    # this is calle keyword argument

# nested function

def outerfunc():
    print("This is the outer function :" )
    def innerfunc():
             print("This is inner function:")
    innerfunc()
outerfunc()                         
# result: This is inner function:
#         This is the outer function : 
# so , here first calls outer func thne after print then excutes inner function inside outer function.
