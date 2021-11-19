def average(array):
    # your code goes here
    m=set(array)

    x=sum(m)
    y=len(m)
    a=x/y
    return round(a,3)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)