def place_marker(board,marker,pos):
 board[pos]=marker
 
test_board=['#','x','o','x','o','x','o','x','o','x']
place_marker(test_board,'$',8)
display_board(test_board)
 