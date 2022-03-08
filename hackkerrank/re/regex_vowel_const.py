import re
pattern=re.compile(r'[aeiou]')
a=input()
if(pattern.match(a)):
    print('voew')

