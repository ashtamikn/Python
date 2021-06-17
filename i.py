class Line():
  def __init__(self,coor1,coor2):
    self.coor1=coor1
    self.coor2=coor2
  def distance(self):
   x1,y1=self.coor1
   x2,y2=self.coor2
   return ((x2-x1)**2+(y2-y1)**2)**0.5
   
  def slope(self):
   x1,y1=self.coor1
   x2,y2=self.coor2
   return (y2-y1)/(x2-x1)
 #   c1=(3,2)
3#>>> c2=(8,10)
#>>> myline=Line(c1,c2)
#>>> myline.distance()
#9.433981132056603
#>>> myine.slope()

   
class Cylinder():
   def __init__(self,height=1,rad=1):
    self.height=height
    self.rad=rad
   def volume(self):
    return self.height*3.14*(self.rad)**2
   def area(self):
    return (2*3.14*(self.rad)**2)+(2*3.14*self.rad*self.height)
class Account():
 def __init__(self,owner,balance):
   self.owner=owner
   self.balance=balance 
   
 def deposit(self,add):
   self.balance=self.balance+add
   print("current balance= {}".format(self.balance))
 def withdraw(self,remove):
   self.balance=self.balance-remove
   print("current balance= {}".format(self.balance))
   acct1=Account('jose',100)
#>>> acct1.deposit(600)
#current balance= 700
#>>> acct1.withdraw(500)
#current balance= 200
 

