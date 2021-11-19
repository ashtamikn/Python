# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
t=int(input())
for _ in range(t):
    s=input()
    if re.match(r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[a-zA-Z0-9]{10}$',s):
        print("Valid")
    else:
        print("Invalid")    
        
        
#         Explanation:

# (?!.*(.).*\1) checks no repeating characters;
# (?=(?:.*[A-Z]){2,}) checks at least 2 uppercase letters;
# (?=(?:.*\d){3,}) checks at least 3 digits;
# [a-zA-Z0-9]{10} checks exactly 10 alphanumeric characters.