def split_and_join(line):
    # write your code here
    s=line.split()
    r='-'.join(s)
    return r
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)



#     >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings. 
# >>> print a
# ['this', 'is', 'a', 'string']
# Joining a string is simple:

# >>> a = "-".join(a)
# >>> print a
# this-is-a-string 