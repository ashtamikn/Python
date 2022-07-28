import sys
from functools import reduce
# from fractions import gcd
from math import gcd

input()
a = map(int,input().strip().split())
b = map(int,input().strip().split())
lcm_a = reduce(lambda x,y: x*y//gcd(x,y), a)
gcd_b = reduce(gcd, b)
print(sum(1 for x in range(lcm_a,gcd_b+1,lcm_a) if gcd_b%x==0))


# reduce(fun,seq) 
# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
# This process continues till no more elements are left in the container.
# The final returned result is returned and printed on console.


# lambda arguments : expression