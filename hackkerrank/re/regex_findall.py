# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

a=re.findall('(?<=[bcdfghjklmnpqrstvwxyz])([aeiou]{2,})[bcdfghjklmnpqrstvwxyz]',input(),re.I)
if a:
  for i in a:
    print(i,end='\n')
else:
    print('-1')    
    
# import re
# s = '[qwrtypsdfghjklzxcvbnm]'
# a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
# print('\n'.join(a or ['-1']))





# re.findall()
# The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings.
# Code

# >>> import re
# >>> re.findall(r'\w','http://www.hackerrank.com/')
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
# re.finditer()
# The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string.
# Code

# >>> import re
# >>> re.finditer(r'\w','http://www.hackerrank.com/')
# <callable-iterator object at 0x0266C790>
# >>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

#  re.I (ignore case)

# (?<=...)
# Matches if the current position in the string is preceded by a match for ... that ends at the current position. This is called a positive lookbehind assertion. (?<=abc)def will find a match in 'abcdef', since the lookbehind will back up 3 characters and check if the contained pattern matches. The contained pattern must only match strings of some fixed length, meaning that abc or a|b are allowed, but a* and a{3,4} are not. Note that patterns which start with positive lookbehind assertions will not match at the beginning of the string being searched; you will most likely want to use the search() function rather than the match() function:

# >>>
# import re
# m = re.se
  # arch('(?<=abc)def', 'abcdef')
  # m.group(0)
  # 'def'
  # This example looks for a word following a hyphen:

# >>>
# m = re.search(r'(?<=-)\w+', 'spam-egg')
# m.group(0)
# 'egg'