import numpy
a=numpy.array(input().split(),int)#numpy.array(list,datatype)
b=numpy.array(input().split(),int)

print (numpy.inner(a, b) )
print (numpy.outer(a, b) )


# A = numpy.array([0, 1])
# B = numpy.array([3, 4])

# print numpy.inner(A, B)     #Output : 4
# A = numpy.array([0, 1])
# B = numpy.array([3, 4])

# print numpy.outer(A, B)     #Output : [[0 0]
#                             #          [3 4]]