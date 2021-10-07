fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    x=line.split()
    for y in x:
        if y not in lst:
            lst.append(y) 
print(sorted(lst))        
#print(line.rstrip())
