if __name__ == '__main__':
    s = input()
    print (any(i.isalnum()  for i in s))
    print (any(i.isalpha() for i in s))
    print (any(i.isdigit() for i in s))
    print (any(i.islower() for i in s))
    print (any(i.isupper() for i in s))
    
    
    # for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
    #     any(eval("c." + test + "()") for c in s)
    
    # for i in s:
    # if i.isalnum():
    #     print(True)
    #     break




# str.isalnum()
# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

# >>> print 'ab123'.isalnum()
# True
# >>> print 'ab123#'.isalnum()
# False
# str.isalpha()
# This method checks if all the characters of a string are alphabetical (a-z and A-Z).

# >>> print 'abcD'.isalpha()
# True
# >>> print 'abcd1'.isalpha()
# False
# str.isdigit()
# This method checks if all the characters of a string are digits (0-9).

# >>> print '1234'.isdigit()
# True
# >>> print '123edsd'.isdigit()
# False
# str.islower()
# This method checks if all the characters of a string are lowercase characters (a-z).

# >>> print 'abcd123#'.islower()
# True
# >>> print 'Abcd123#'.islower()
# False
# str.isupper()
# This method checks if all the characters of a string are uppercase characters (A-Z).

# >>> print 'ABCD123#'.isupper()
# True
# >>> print 'Abcd123#'.isupper()
# False