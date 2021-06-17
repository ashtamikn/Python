try:
 f=open('testfile','w')
 f.write("write a test line")
 
except TypeError:
 print('ther was a type error')
 
except OSError:
 print('hey you an os error')
finally:
 print('i always run') 
 
def ask_for_int():
 while True:
 
  try:
   result=int(input('please provide no'))
  except:
   print('thats not no')
   continue
  else:
   print('yes no')
   break 
  finally:
   print("end of try")
  
  

for i in ['a','b','c']:
  try:
    print(i**2)
  except:
    print('thos are not nos')
  
try:
 x=5
 y=0
 z=x/y
 print(z)
except:
 print("not defined")
finally:
 print("all done")
 
def ask():
  while True:
   try:
     a=int(input('provide no'))
     z=a*a
     print(z)
   except:
     print('invalid no')
   else:
     print('yr no squareed is {}'.format(z))    
  a=1
  b=2
  
