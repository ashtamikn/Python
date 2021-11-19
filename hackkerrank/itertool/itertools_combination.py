from itertools import combinations
string, n = input().split()
for i in range(1,int(n)+1):
    data = ["".join(sorted(i)) for i in combinations(string,i)]
    data.sort()
    print("\n".join(data))
