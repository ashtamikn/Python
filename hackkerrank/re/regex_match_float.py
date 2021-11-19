import re
n=int(input())
pattern=re.compile("^[+-]?[0-9]*[\.][0-9]+$")
for i in range(n):
    s=input()
    if pattern.match(s):
        print("True")
    else:
        print("False")
        