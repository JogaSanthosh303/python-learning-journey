# string is nothing but collection of characters
""" 
string can write in single quote, double quote and triple quote but 
a string with apostrophe like sons's etc won't be write in single quote so double quote Use
for multi line words like that triple quote is preferred. for exmaple: """

a= 'b';
singlequote = 'words'
doubleQuote="Santhosh's life"
tripleQUote= """ pyhton 
java 
c language
maven
 """
print(type(singlequote), type(doubleQuote), type(tripleQUote))
# output : <class 'str'> <class 'str'> <class 'str'>


#String methods
""" lower , upper, endswith , startswith , replace , find, index, count, remove prefix, 
remove suffix, split, strip, rstrip, lstrip """

abc= "JAVA LANGUAGE"
xyz= "   python   "

print(abc.lower())
print(xyz.upper())
print(abc.startswith('p') , xyz.endswith('n'))
print(abc.replace('LANGUAGE' , 'PROGRAMMING'))
print(abc.find('E') , abc.index('L'))  
# Both return the position of a substring, but find() returns -1 if not found, whereas index() raises an exception

print(abc.count('G'))
print(abc.removeprefix('JAVA') , abc.removesuffix('LANGUAGE'))
print(abc.split())
print(len(xyz))
print(xyz.strip())
print(xyz.lstrip())
print(xyz.rstrip())


