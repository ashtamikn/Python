import random
suits=('hearts','diamonds','spades','clubs')
ranks=('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')

values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,
'ace':11}
playing=True
 

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
 def __str__(self):
    deck_comp=''
    for card in self.all_cards:
     deck_comp+='\n'+card.__str__()
     return"the deck has "+ deck_comp       
         
 def shuffle(self):
   random.shuffle(self.all_cards)
   
 def deal_one(self):
   single_card=self.all_cards.pop() 
   return self.all_cards.pop()
   
class Hand:
    def __init__(self):
       self.cards=[]
       self.value=0
       self.aces=0
    def add_card(self,card):
       self.cards.append(card)
       self.value+=values[card.rank]     
       
       
       if card.rank=='ace':
         self.aces+=1
    def adjust_for_ace(self):
       while self.value>21 and self.aces>0:
         self.value-=10
         self.aces-=1    
         
class Chips:
 def __init__(self,total=100):
    self.total=total
    self.bet=0         
         
 def win_bet(self):
    self.total+=self.bet
    
 def lose_bet(self):
    self.total-=self.bet           
    
    
def take_bet(chips):
  while True:
    try:
      chips.bet=int(input('how many chips would you like to bet?'))
    except:
      print('sorry please provide an integer')
    else:
      if chips.bet>chips.total:
        print('sorry,you do not have enough chips! you have{}'.format(chips.total))
      else:
        break
        
def hit(deck,hand):
   single_card=deck.deal_one()
   hand.add_card(single_card)
   hand.adjust_for_ace()
   
def hit_or_stand(deck,hand):
   playing=True
   while playing==True:
     x=input('hit or stand? enter h or s')
     if x[0].lower()=='h':
        hit(deck,hand)
     elif x[0].lower()=='s':
        print('player stands dealer turn')
        playing=False
     else:
        print('sorry ,i didnt understand ,please enter h or s only')
        continue
        break
def show_some(player,dealer):
   print('dealers hand')
   print('one card hidden')
   print(dealer.cards[1])
   print('\n')
   print('player hand:')
   for card in player.cards:
      print(card)   
      
def show_all(player,dealer):
   print('dealer hand')
   for card in dealer.cards:
     print(card)
   print('player hand')
   for card in player.cards:
     print(card)               
        
        
def player_busts(player,dealer,chips):
    print('bust player')
    chips.lose_bet()
       
def player_wins(player,dealer,chips):
    print('player wins')
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print('player wins!dealer busted!')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('bust player,dealer wins')
    chips.lose_bet()

def push(player,dealer):                       
   print('dealer and player tie push')
   
   
while True:
   print('welcome to black jack')
   deck=Deck()
   deck.shuffle()
   
   player_hand=Hand()
   player_hand.add_card(deck.deal_one())
   player_hand.add_card(deck.deal_one())
         
   dealer_hand=Hand()
   dealer_hand.add_card(deck.deal_one())
   dealer_hand.add_card(deck.deal_one())
      
   player_chips=Chips()
   
   take_bet(player_chips)
   
   show_some(player_hand,dealer_hand)
   while playing==True:
     hit_or_stand(deck,player_hand)
     show_some(player_hand,dealer_hand)
     if player_hand.value>21:
        player_busts(player_hand,dealer_hand,player_chips)
        break
   if player_hand.value<=21:
     while dealer_hand.value<17:
        hit(deck,dealer_hand)
          
     show_all(player_hand,dealer_hand)
     if dealer_hand.value>21:
        dealer_busts(player_hand,dealer_hand,player_chips)
     elif dealer_hand.value>player_hand.value:
        dealer_wins(player_hand,dealer_hand,player_chips)  
     elif dealer_hand.value<player_hand.value:
        player_wins(player_hand,dealer_hand,player_chips)  
     else:
        push(player_hand,dealer_hand)
          
   print('\n player total chips are at {}'.format(player_chips.total))
   
   new_game=input('want to play again? y or n')
   
   if new_game[0].lower()=='y':
      playing=True
      continue
   else:
      print('thank you')
      break  
            
