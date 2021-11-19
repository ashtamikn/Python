l = []
second_lowest_names = []
scores = set()

for _ in range(int(input())):
    name = input()
    score = float(input())
    l.append([name, score])
    scores.add(score)
# print(scores)       
second_lowest = sorted(scores)[1]

for name, score in l:
    if score == second_lowest:
        second_lowest_names.append(name)

for name in sorted(second_lowest_names):
    print(name, end='\n')


    # if __name__ == '__main__':
    # L=[]
    # n=int(input())
    # for _ in range(n):
    #     name = input()
    #     score = float(input())
    #     L.append([name,score])
    # k=[]
    # for i in range(n):
    #     k.append(L[i][1])
    
    # k.sort()
        
    # i=1
    # while i<n and k[0]==k[i]:
    #     i=i+1
    # m=k[i]
    # s=[]
    # for j in range(n):
    #     if L[j][1]==m:
    #         s.append(L[j][0])
    # s.sort()
    # for z in range(len(s)):
    #  print(s[z])
