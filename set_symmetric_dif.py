m=int(input())
s=set(input().split())
n=int(input())
t=set(input().split())
print(len(s-t))

# >>> s = set("Hacker")
# >>> print s.symmetric_difference("Rank")
# set(['c', 'e', 'H', 'n', 'R', 'r'])

# >>> print s.symmetric_difference(set(['R', 'a', 'n', 'k']))
# set(['c', 'e', 'H', 'n', 'R', 'r'])

# >>> print s.symmetric_difference(['R', 'a', 'n', 'k'])
# set(['c', 'e', 'H', 'n', 'R', 'r'])

# >>> print s.symmetric_difference(enumerate(['R', 'a', 'n', 'k']))
# set(['a', 'c', 'e', 'H', (0, 'R'), 'r', (2, 'n'), 'k', (1, 'a'), (3, 'k')])

# >>> print s.symmetric_difference({"Rank":1})
# set(['a', 'c', 'e', 'H', 'k', 'Rank', 'r'])

# >>> s ^ set("Rank")
# set(['c', 'e', 'H', 'n', 'R', 'r'])
