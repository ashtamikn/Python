import string
def print_rangoli(size):
    alp  = string.ascii_lowercase

    for i in range(size-1,-size,-1):#4:-4:-1
        pattern = '-'.join(alp[size-1:abs(i):-1]+alp[abs(i):size])
        print(pattern.center(4*size-3,'-'))#The width of a rangoli of size 5 is 5*4-3 which is n*4-3
        
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)