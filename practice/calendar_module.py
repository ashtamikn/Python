# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime
import calendar
m,d,y=map(int,input().split())
my_date=datetime.date(y,m,d)
print(calendar.day_name[my_date.weekday()])

# print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())

# to get name of day(in number) from date
# print('Day of Week (number): ', my_date.weekday())

# to get name of day from date
# print('Day of Week (name): ', calendar.day_name[my_date.weekday()])