# group()
# A group() expression returns one or more subgroups of the match.
# Code

# >>> import re
# >>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
# >>> m.group(0)       # The entire match 
# 'username@hackerrank.com'
# >>> m.group(1)       # The first parenthesized subgroup.
# 'username'
# >>> m.group(2)       # The second parenthesized subgroup.
# 'hackerrank'
# >>> m.group(3)       # The third parenthesized subgroup.
# 'com'
# >>> m.group(1,2,3)   # Multiple arguments give us a tuple.
# ('username', 'hackerrank', 'com')
# groups()
# A groups() expression returns a tuple containing all the subgroups of the match.
# Code

# >>> import re
# >>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
# >>> m.groups()
# ('username', 'hackerrank', 'com')
# groupdict()
# A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name.
# Code

# >>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
# >>> m.groupdict()
# {'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}

import re
s=input()
m=re.search(r'([a-zA-Z0-9])\1+',s.strip())#in grp 1 if you get 3 \1+=>3 is repeated more or equal to once
print(m.group(1) if m else -1)

# \number===backreferences
# \1=>char in grp 1 is repeated
# \2=>char in grp 2 is repeated and can be used anywhere

# Matches the contents of the group of the same number. Groups are numbered starting from 1
# . For example, (.+) \1 matches 'the the' or '55 55', but not 'thethe' (note the space after the group). 
# This special sequence can only be used to match one of the first 99 groups. If the first digit of number is 0, 
# or number is 3 octal digits long, it will not be interpreted as a group match, but as the character with octal value number. 
# Inside the '[' and ']' of a character class, all numeric escapes are treated as characters.

