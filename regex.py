# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    ans = True
    try:
        reg = re.compile(input())
    except re.error:
        ans = False
    print(ans)
    # len(re.findall(pattern, string)) that returns the number of matching substrings or 
    # len([*re.finditer(pattern, text)]) that unpacks all matching substrings into a list and returns the length of it as well.

