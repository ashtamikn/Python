import random
suits=('hearts','diamonds','spades','clubs')
ranks=('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')

values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':11,'queen':12,'king':13,
'ace':14}
  
class Card:
  def __init__(self,suit,rank):                                  
    self.suit=suit
    self.rank=rank
    self.value=values[rank]
  def __str__(self):
    return self.rank+" of " +self.suit  
   
class Deck:
 def __init__(self):
    self.all_cards=[]
    for suit in suits:
     for rank in ranks:
         created_card=Card(suit,rank)
         self.all_cards.append(created_card)
         
 def shuffle(self):
   random.shuffle(self.all_cards)
   
 def deal_one(self):
   return self.all_cards.pop()
 
class Player:
  def __init__(self,name):
     self.name=name
     self.all_cards=[]
     
  def remove_one(self):
     return self.all_cards.pop(0)
  def add_cards(self,new_cards):
     if type(new_cards)==type([]):
       self.all_cards.extend(new_cards)
     else:
       self.all_cards.append(new_cards)  
  def __str__(self):
     return 'player {} has {} cards'.format(self.name,len(self.all_cards))            
 
 
player_one=Player('one')
player_two=Player('two')

new_deck=Deck()
new_deck.shuffle()

for x in range(26):
  player_one.add_cards(new_deck.deal_one()) 
  player_two.add_cards(new_deck.deal_one()) 
  
 
game_on=True
round_num=0

while game_on:
  round_num+=1
  print('round  {}'.format(round_num))    
  
  if len(player_one.all_cards)==0:
    print('player 1 is out of cards,player 2 wins')
    game_on=False
    break
   
  if len(player_two.all_cards)==0:
    print('player 2 is out of cards,player 1 wins')
    game_on=False
    break 

  player_one_cards=[]
  player_one_cards.append(player_one.remove_one())
 
  player_two_cards=[] 
  player_two_cards.append(player_two.remove_one())
    

  at_war=True
  while at_war:
   if player_one_cards[-1].value>player_two_cards[-1].value:
     player_one.add_cards(player_one_cards)
     player_one.add_cards(player_two_cards)
     at_war=False
     
   elif player_one_cards[-1].value<player_two_cards[-1].value: 
     player_two.add_cards(player_one_cards)
     player_two.add_cards(player_two_cards)
     at_war=False
     
   else:
     print('war!!!')
     
     if len(player_one.all_cards)<5:
       print('player 1 looses  ')
       print('player 2 wins')
       game_on=False
       break
     
     if len(player_two.all_cards)<5:
       print('player 2 looses  ')
       print('player 1 wins')
       game_on=False
       break
     else:
       for num in range(3):
          player_one_cards.append(player_one.remove_one()) 
          player_two_cards.append(player_two.remove_one())
     
     
     
     
     
#( new_deck=Deck()

#>>> two_hearts
#<__main__.Card object at 0x7ff09c54b128>
#>>> print(two_hearts)
#two of hearts

