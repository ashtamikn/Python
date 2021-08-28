# Enter your code here. Read input from STDIN. Print output to STDOUTimport numpy
import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)],int)
x=numpy.sum(A, axis=0)
print(numpy.prod(x, axis=0))
# my_array = numpy.array([ [1, 2], [3, 4] ])

# print numpy.sum(my_array, axis = 0)         #Output : [4 6]
# print numpy.sum(my_array, axis = 1)         #Output : [3 7]
# print numpy.sum(my_array, axis = None)      #Output : 10
# my_array = numpy.array([ [1, 2], [3, 4] ])

# print numpy.prod(my_array, axis = 0)            #Output : [3 8]
# print numpy.prod(my_array, axis = 1)            #Output : [ 2 12]
# print numpy.prod(my_array, axis = None)         #Output : 24
# print numpy.prod(my_array)                      #Output : 24