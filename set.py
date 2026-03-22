""" 
{}
Do not allow dupliactes 
no index, un ordered
do not allow mutable types as set elements

set method: 
add() , update(), pop() , remove()

set operater: 
union() , intersection() , difference() , isSubset() , isSuperset()
 

"""
# set methods 
s={2,5,6,8,8,9}
print(s)
s.update({"Java" , "python"})    # here it used for bulk update
s.update({55,66,99})
s.add('language')                # add method only takes one value but update takes bulk values 
print(s)

print(s.pop())         # here pop method will remove any random element bcoz set is  unorderd
s.remove(66)
print(s)

# set operations'
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.union(s2))         # o/p : {1, 2, 3, 4, 5, 6, 7, 8}
print(s1.intersection(s2))  # o/p : {4, 5}
print(s1.difference(s2))    # o/p : {1, 2, 3}   here common data will deleted and print only s1 data

print(s1.issubset(s2))      # false
print(s1.issuperset(s2))    # false

s3={1,2,3}
s4={1,2,3,4,5}
print(s3.issubset(s4))       # true
print(s3.issuperset(s4))     # false
print(s4.issuperset(s3))     # true
    