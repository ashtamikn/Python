
    
class Dog(Animal):
  def __init__(self):
    Animal.__init__(self)
    print('dog created')
    
  def who_am_i(self):
    print('i am dog')
class Book():
  def __init__(self,title,author,pages):#b=Book('t','a',2)
    self.title=title
    self.author=author
    self.pages=pages
  def __str__(self):#print(b) gives this
    return "{} by {} ".format(self.title,self.author)
  def __len__(self):#len(b) givs this
    return self.pages 
  def __del__(self):# to delete book
     print('a book deleted')
