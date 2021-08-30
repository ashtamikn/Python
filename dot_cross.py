import numpy
n=(int(input()))
A=numpy.array([input().split() for _ in range(n)],int)
B=numpy.array([input().split() for _ in range(n)],int)
m=numpy.dot(A,B)
print(m)



# A = numpy.array([ 1, 2 ])
# B = numpy.array([ 3, 4 ])

# print numpy.dot(A, B)       #Output : 11
# A = numpy.array([ 1, 2 ])
# B = numpy.array([ 3, 4 ])

# print numpy.cross(A, B)     #Output : -2