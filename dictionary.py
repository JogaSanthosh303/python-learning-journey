""" 
{}
key, value data (k:v)
key should be immutable
value should be mutablr(diff types)
key will acts as index
no slicing
keys are unique

example : a={'a':123 , b:"456"}  , here key and value pair and combination of key and value pair is item.

Dict methods:
get()
update()
values()
keys()
items()
"""

d={}
print(type(d))   # eg: <class 'dict'>

d= {1:'abc' , 'santhosh': 303}
print(d.get(1))   # o/p: abc
print(d.get("santhosh"))
print(d.keys() , d.values())
print(d.items())
d.update({3:"added"})
print(d)

for i in d.keys():
    print(i)         # only keys will iterate and print

for i in d.values():
    print(i)         # only values will iterate and print'

for i in d.items():  # both keys and values will be print
    print(i)         # (1, 'abc')  ('santhosh', 303)  (3, 'added')  

for i , j in d.items():   
    print(i,j)        # print keys and values seperately like i prints keys and j prints values
