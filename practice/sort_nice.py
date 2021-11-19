N, M = map(int, input().split())
rows = [input() for _ in range(N)]
K = int(input())

for row in sorted(rows, key=lambda row: int(row.split()[K])):
    #sorted(iterable, key=None, reverse=False)
    print(row)


#     In [9]: mylist = [(3, 5, 8), (6, 2, 8), (2, 9, 4), (6, 8, 5)]
# In[10]: sorted(mylist, key=lambda x: x[1])
# My sorted call obviously says, "Please sort this list". The key argument makes that a little more specific by saying, 'for each element x in mylist, return the second index of that element, then sort all of the elements of the original list mylist by the sorted order of the list calculated by the lambda function. Since we have a list of tuples, we can return an indexed element from that tuple using the lambda function.

# The pointer that will be used to sort would be:

# [5, 2, 9, 8] # the second element of each tuple
# Sorting this pointer list returns:

# [2, 5, 8, 9]
# Applying this to mylist, we get:

# Out[10]: [(6, 2, 8), (3, 5, 8), (6, 8, 5), (2, 9, 4)]