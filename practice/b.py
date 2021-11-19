def player_input():
 marker=''
 while marker!='x' and marker!='o':
  marker=input('player 1,choose x or o:').upper()
  player1=marker
  if player1=='x':
     player2='o'
  else:
     player2='x'
  return(player1,player2)   
player_input()
