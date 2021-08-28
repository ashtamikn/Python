# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
numpy.set_printoptions(legacy='1.13')
nums=tuple(map(int,input().split()))
m=nums[0]
n=nums[1]
print (numpy.eye(m, n, k = 0))    # m X n Dimensional array with first default diagonal 1.
