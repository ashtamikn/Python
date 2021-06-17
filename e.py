class Dog():
   species='mammal'#class attribute
   def __init__(self,mybreed,name):#to call this attributes u dont use ()
     self.breed=mybreed
     self.name=name
     
   def bark(self,number):#to call this method u have to use ()
     print('woof,my name is {} and number ics {}'.format(self.name,number))
my_dog=Dog(mybreed='lab',name='sammy',spots=False)


class Animal():
 def __init__(self,name):
    self.name=name
    
 def speak(self):
    raise NotImplementedError("subclass must implement this abstract method")
    
class Cat(Animal):
   def speak(self):
     return self.name+" says meow"

