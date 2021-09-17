l1 = ["eat","sleep","repeat"]
 
# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)

# changing index and printing separately
for count,ele in enumerate(l1,100):
    print (count,ele)
 
#getting desired output from tuple
for count,ele in enumerate(l1):
  print(count)
  print(ele)

#   Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object. This enumerated object can then be used directly for loops or converted into a list of tuples using the list() method.
#   Syntax: 

# enumerate(iterable, start=0)
