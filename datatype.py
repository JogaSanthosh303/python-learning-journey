""" 
int
float
string
boolean
complex

 """

a = 123
x=-33
b="words"
c=2.3
d=True
e= 2 + 3j
print(type(a) , type(x) , type(b) , type(c) , type(d) , type(e)) 

# output : <class 'int'> <class 'int'> <class 'str'> <class 'float'> <class 'bool'> <class 'complex'>

""" 
Type conversion
int()
float()
bool()
str()

 """
v = 2
print(float(v))     # result -> 2.0

# here  after type conversion , value changes from 2.0 to 2 
# so no data lose means implicit type conversion

f= float(v)
print(type(f))      # result -> <class 'float'>

v=5.5
print(int(v))       # result -> 5

# here after type conversion value is changes from 5.5 to 5 . 
# so data lose means explicit type conversion

