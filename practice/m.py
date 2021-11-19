def hello(name='jose'):
    print('hello func is been executed')
    def greet():
      return '\t this is greet func inside hello'
   
    def welcome():
      return'\t this is welcome indside hello' 
    if name=='jose':
      return greet
    else:
      return welcome  
def cool():
  def super_cool():
    return'i am cool'
  return super_cool()
  
def hello():
  return 'hi jose'
def other(fhfj_kk):
  print('some code')
  print(fhfj_kk())
  
def new_decorator(original_func):
  def wrap_func():
    print('some code before of')
    original_func()
    print('some code after of')
    
  return wrap_func    
@new_decorator
      
def func_needs_decorator():
  print('want to bedecorato')

def create_cubes(n):
 result=[]
 for x in range(n):
   result.append(x**3)
 return result  
   
   >>> def create_cubes(n):
...  for x in range(n):
...   yield x**3
... 
>>> create_cubes(10)
<generator object create_cubes at 0x7fe533e53f78>
>>> list(create_cubes(10))
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>> 
>>> def simple_gen():
...   for x in range(3):
...     yield x
... 
>>> for number in simple_gen():
...  print(number)
... 
0
1
2
>>> g=simple_gen()
>>> g
<generator object simple_gen at 0x7fe530457438>
>>> print(next(g))
0
>>> 
>>> print(next(g))
1
>>> print(next(g))
2
>>> print(next(g))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> 
def gensquares(n):
  for i in range(n):
    yield i**2
    
for x in gensquares(10):
  print(x)   
    
import random

def rand_num(low,high,n):
  for i in range(n):
    yield random.randint(low,high)
    
    
for v in rand_num(1,10,12):
 print(v)
 
from collections import Counter
 >>> mylist=[1,,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4]
  File "<stdin>", line 1
    mylist=[1,,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4]
              ^
SyntaxError: invalid syntax
>>> mylist=[1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4]
>>> Counter(mylist)
Counter({1: 7, 2: 5, 3: 4, 4: 1})
>>> from collections import defaultdict
>>> d={'a':10}
>>> d
{'a': 10}
>>> d['a']
10
>>> d['hj']=0
>>> d['hj']
0
>>> d['hj']=098
  File "<stdin>", line 1
    d['hj']=098
              ^
SyntaxError: invalid token
>>> d['hj']=98
>>> d['hj']
98
>>> d=defaultdict(lambda:0)
>>> d['k']
0
 from collections import namedtuple
>>> dog=namedtuple('dog',['age','breed','name'])
>>> sammy=dog(age=5,breed='husky',name='sam')
>>> type(sammy)
<class '__main__.dog'>
>>> sammy
dog(age=5, breed='husky', name='sam')
>>> sammy.age
5
>>> sammy[0]
5
>>> sammy.breed
'husky'
>>> sammy[1]
'husky'
>>> import datetime
>>> mt=datetime.time
>>> mt=datetime.time(2,20)
>>> mt.minute
20
>>> mt.hour
2
>>> print(mt)
02:20:00
 from datetime import date
>>> date1=date(2021,11,3)
>>> date2=date(2020,11,3)
>>> date1-date2
datetime.timedelta(365)
>>> datetime1=datetime(2021,11,3,22,0)
>>> datetime2=datetime(2020,11,3,12,0)'
  File "<stdin>", line 1
    datetime2=datetime(2020,11,3,12,0)'
                                      ^
SyntaxError: EOL while scanning string literal
>>> datetime2=datetime(2020,11,3,12,0)
>>> datetime1-datetime2
datetime.timedelta(365, 36000)

     
