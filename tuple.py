""" 
() parenthesis
allow diff types of elements
allow duplicates
aloow indexing an slicing
immutable ( notchangable so data not modified so no need to builtin methods in tuple)
no methods we can use builtin """

tuple=(1,5,9,8)

print(tuple[2])    #o/p : 9

print(tuple[0:3:2])

#tuple has no predefined methods due to immutable but we can perform operations using general methods
print(min(tuple))
print(max(tuple))
print(sum(tuple) , len(tuple))

#concatnation
t1=(1,2,3)
t2 = (4,5,6,7)
t3=t1+t2
print(t3)    # o/p : (1, 2, 3, 4, 5, 6, 7)

# repetion
t=(1,5,7,9)
print(t*3)    # o/p : (1, 5, 7, 9, 1, 5, 7, 9, 1, 5, 7, 9)

#iteration
for i in t:
    print(i)

 # membership  i.e., it will check the value prsent in it or not
    print(9 in t)         # true
    print(24 not in t)    # true
    print(8 in t)         # false

    print(t1 is t2)
    print(t1 is not t2)  
