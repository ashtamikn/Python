from collections import namedtuple
n, Score = int(input()) , namedtuple('Score',input().split())
scores = [Score(*input().split()).MARKS for i in range(n)]
print("{:.2f}".format(sum(map(int,scores))/n))