import one
print("top level in two.py")
one.func()
if __name__=='__main__':
 print("two.pyis being rundirectly") 
else:
 print('to.py has imported')
