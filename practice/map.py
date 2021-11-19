if __name__ == '__main__':
    n = int(input())
    nums = map(int, input().split())    
    print (sorted(list(set(nums)))[-2])
    # The original numbers variable is unchanged because sorted() provides sorted output and does not change the original value in place.
# When sorted() is called, it provides an ordered list as a return value.