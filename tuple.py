n = int(input())
integer_list = map(int, input().split()) 
t=tuple(integer_list)
print (hash(t))
# We need to read the first line of input to get it out of the way (it can be used to write a parser for the next line, but it isn't useful)
# n = raw_input()
# Read in the second line -- this is just a single string ex. '1 2 3 4'
# input_line = raw_input()
# Split the string by whitespace into a list
# input_list = input_line.split()
# Note: This is a list of strings ex. ['1', '2', '3', '4'] But we want a list of integers ex. [1, 2, 3, 4]
# We need to convert the list elements from strings to ints
# [Simple] Option 1 (since we know the number of elements, n):
#     for i in xrange(n):
#         input_list[i] = int(input_list[i])
# [Simple] Option 2 (if we are ignoring the first input line for some reason):
#     for i in xrange(len(input_list)):
#         input_list[i] = int(input_list[i])
# [More Advanced] Option 3:
#     input_list = map(int, input_list)