fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
lst=[]
count = 0
for line in fh:
        if line.startswith("From") and len(line.split())>2:
                s=line.split()
          
                lst.append(s[1])
                print(s[1])

print("There were", len(lst), "lines in the file with From as the first word")