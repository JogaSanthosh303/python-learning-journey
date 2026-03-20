# variable is like a container to store the values 


"""  
Rules for variable:
1. can start with alphabets
2. cannot start with numerics
3. can start with _underscore
4. case senstive 

"""


# single value assigned to single variable
a=10
print(a)


# mutliple values assigned to single variable
c  = 1,2, 4
word = "  | name"
_underscore = "  | variable can start with underscore also"
print(c  , word , _underscore)


# multiple values assigned to multiple varibles
a,b,c = 2, 5, 1
print(b,c,a)


# single value assigned to multiple variables
x=y=z=4
print(y,x,z)

# To find IP address or reference of value then use id method

abc = 123

print(id(abc))

