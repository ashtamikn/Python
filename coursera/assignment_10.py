name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts=dict()
lst=[]
for line in handle:
    if line.startswith("From")and len(line.split())>2:
        words=line.split()
        req=words[5].split(":")
        counts[req[0]]=counts.get(req[0],0)+1
        
        
for k,v in counts.items():
  lst.append((k,v))
    
lst.sort()
for k,v in lst:
    print(k,v)
