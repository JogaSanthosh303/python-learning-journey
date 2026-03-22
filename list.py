
""" 
[ ]
mutable data type
store different types of elements
allow duplicates
allow indexing """list = [1,4,5,2,4,2,9]

print(list)

print(list[2])    #Indexing 

print(list[-1])  # here, indexing start from 0 from left to right 
                 # and starts from -1 from rigth to left

print(list[0:6:2])  #slicing [start index: stop index: skip]       o/p : [1, 5, 4]

""" 
Important methods in list 

append , extend , count , insert , pop , remove


"""
list = [1,4,5,2,4,2,9]
print(list)
print(list.append('santhosh'))       # o/p : none  bcoz append modify object directly . Adds whole item                                                                                                   
print(list.extend([12,2,3]))         # o/p : none  bcoz extend modify object directly . Adds elements one by one
print(list)                          # o/p : [1, 4, 5, 2, 4, 2, 9, 'santhosh', 12, 2, 3]
print(list.remove(2))                # it removes first occurance
myList= [x for x in list if x != 2]  # Using list comprehension to removes all occurrences
print(myList)                        # it removes all 2 values

print(list.count(9))                 # count is used for count no of times that value appears i list

list.insert(2,'hi')                 # we can insert data in a specific index in a list
print(list)

print(list.pop())                  # remove and return vale at last index
print(list)

for i in list:
    print(i)

