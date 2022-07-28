import sys
# 999=27=9
def sumdegits(n):
    s=sys.maxsize
    r=0
    # print(n)
    while(s>10):
        s=0
        while(n>0):
            r=n%10
            s+=r
            n//=10
        n=s
        print(n)
    print(s)

degit=int(input())
sumdegits(degit)
