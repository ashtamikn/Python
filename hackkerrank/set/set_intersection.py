# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
s=set(input().split())
n=int(input())
t=set(input().split())
print(len(s&t))


# >>> s = set("Hacker")
# >>> print s.intersection("Rank")
# set(['a', 'k'])

# >>> print s.intersection(set(['R', 'a', 'n', 'k']))
# set(['a', 'k'])

# >>> print s.intersection(['R', 'a', 'n', 'k'])
# set(['a', 'k'])

# >>> print s.intersection(enumerate(['R', 'a', 'n', 'k']))
# set([])

# >>> print s.intersection({"Rank":1})
# set([])

# >>> s & set("Rank")
# set(['a', 'k'])