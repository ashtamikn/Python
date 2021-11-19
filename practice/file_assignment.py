# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for c in fh:
   c=c.rstrip()
   c=c.upper()
   print(c) 