# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
numpy.set_printoptions(legacy='1.13')
a = numpy.array(input().split(),float)
print(numpy.floor(a))#The tool floor returns the floor of the input element-wise.for 1.1 gives 1
print(numpy.ceil(a))#The tool ceil returns the ceiling of the input element-wise.for 1.1 gives 2

print(numpy.rint(a))#The rint tool rounds to the nearest integer of input element-wise.for 1.1 gives 1 and for 9.9 gives 10

