""" 
open

file read/write operations

close

 """
# Read operation
s=open('sampleFile.txt' ,   mode = 'r')
print(s.read())                          # here it prints the data present the file.
s.close()

# write operation
s=open("sampleFile.txt" , mode='w')
print(s.write("Im a backend deveoper"))   # it truncates the data and replace with the given data in the file
s.close                                

# write operation but need to append the data not truncated the existing data then used append mode

s=open("sampleFile.txt" , mode= 'a')
print(s.write(". Now upgrading to become a full stack developer. "))

""" now if we want both read and write operation then use r+ and w+ mode. 
if first want read operation and then write then use r+ and vice versa use w+. """

s=open('sampleFile.txt' ,   mode = 'r+')
print(s.read())                       # here first read operation and then write operation. no truncate just append
s.write(" now we can do both read and write operations")                       # here it prints the data present the file.
s.close()


s=open('sampleFile.txt' ,   mode = 'w+')
s.write(" now write and read  operations but truncate possible ")  
print(s.read())                       # here first read operation and then write operation. no truncate just append                  # here it prints the data present the file.
s.close()

# in cose , it wont show in read operation after truncate and rite operation done in the above method in file
# if you want to print in console by file pointer change, use seek(0) before read operation




s=open('sampleFile.txt' ,   mode = 'w+')
s.write(" now write and read  operations but truncate possible ")  
s.seek(0)                     # it shows the file chnaged file content in console
print(s.read())               # here first write operation and then read operation.                 # here it prints the data present the file.
s.close()

