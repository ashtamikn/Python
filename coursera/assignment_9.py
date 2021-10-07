name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts=dict()

for line in handle:
    if line.startswith("From") and len(line.split())>2:
        words=line.split()
        counts[words[1]]=counts.get(words[1],0)+1
        
max_val=None
max_author=None
for key in counts:
    if max_val==None or counts[key]>max_val:
        max_val=counts[key]
        max_author=key
        
print(max_author,max_val)        
        
