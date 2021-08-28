# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
N, M = map(int, input().split())
A=numpy.array([input().split() for _ in range (N)],int)
x=numpy.min(A,axis=1)
print(numpy.max(x))

# my_array = numpy.array([[2, 5], 
#                         [3, 7],
#                         [1, 3],
#                         [4, 0]])

# print numpy.min(my_array, axis = 0)         #Output : [1 0]
# print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
# print numpy.min(my_array, axis = None)      #Output : 0
# print numpy.min(my_array)                   #Output : 0
# my_array = numpy.array([[2, 5], 
#                         [3, 7],
#                         [1, 3],
#                         [4, 0]])

# print numpy.max(my_array, axis = 0)         #Output : [4 7]
# print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
# print numpy.max(my_array, axis = None)      #Output : 7
# print numpy.max(my_array)                   #Output : 7