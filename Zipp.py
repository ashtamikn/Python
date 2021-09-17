n, x = map(int, input().split()) 

sheet = []
for _ in range(x):
    sheet.append( map(float, input().split()) ) 

for i in zip(*sheet): 
    #sheet alliro main lsit na unpack  maadi ...hosdaag add aagirov na zip madutte
    print( sum(i)/len(i) )