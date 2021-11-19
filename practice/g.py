class Animal():
 def __init__(self):
    print('animal created')
 def who_am_i(self):
    print('animal')
 def eat(self):
    print('eating')
    
    
class Dog(Animal):
  def __init__(self):
    Animal.__init__(self)
    print('dog created')
  def eat(self):
    print('i am  a dog and eating')  
  def who_am_i(self):
    print('i am dog')
    
  def bark(self):
     print('woof')  
     
class Dog():
  def __init__(self,name):
    self.name=name
  def speak(self):
    return self.name + "says woof"
    
class Cat():
  def __init__(self,name):
    self.name=name
  def speak(self):
    return self.name + "says meow"
    
for pet in [niko,felix]:
   print(pet.speak())
def pet_speak(pet):
  print(pet.speak())
  
