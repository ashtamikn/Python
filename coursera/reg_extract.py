import re;
line='from ashi@me.com '
y=re.findall("(^from ).*@([^ ]*)",line)
# (whatever inside this bracket is stored in y)
print(y)