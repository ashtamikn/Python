def characterReplacement(s,k):
    count={}
    # it keeps count of each alphabet
    res=0
    left=0
    for right in range(len(s)):
        count[s[right]]=1+count.get(s[right],0)
        print(count)
        while (right-left+1)-max(count.values())>k:
            count[s[left]]-=1
            left+=1
        print(max(res,right-left+1))
        res=max(res,right-left+1)
    return res

st=input()
print(st)

k=int(input())
print(k)
x=characterReplacement(st,k)
print(x)

