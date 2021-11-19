# As you know, input().split() splits the input multiple items where ever there is a space separator. 'Banana Fries 60' gets separated into 'Banana' 'Fries' and '60'

# *item_name,price = input().split()

# Now this line assigns the last item to price and combines the rest of items as a list and assigns to item_name
# https://www.datacamp.com/community/tutorials/usage-asterisks-python
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n=int(input())
dicti=OrderedDict()
for i in range(n):
    *k,v=input().split()
    k=' '.join(k)
    dicti[k]=dicti.get(k,0)+int(v)#gets k value adds v to it if already exists...else default it takes 0 and adds v  to it
for k,v in dicti.items():
    print(k,v)    
#     from collections import OrderedDict
# d = OrderedDict()
# for _ in range(int(input())):
#     item, space, quantity = input().rpartition(' ')
#     d[item] = d.get(item, 0) + int(quantity)
# for item, quantity in d.items():
#     print(item, quantity)