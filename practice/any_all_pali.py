m,a=int(input()),(input().split())
print(all([int(i)>0 for i in a])and any([i==i[::-1] for i in a]))