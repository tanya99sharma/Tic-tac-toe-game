#function that prints out a board

def display_board(board):
    
   
    print('  ' + '|' + '   ' + '|')
    print(board[7] + ' ' + '|'+ ' ' + board[8]+ ' ' + '|'+ ' ' + board[9])
    print('  ' + '|' + '   ' + '|')
    print('---------')
    print('  ' + '|' + '   ' + '|')
    print(board[4] + ' ' + '|'+ ' ' + board[5]+ ' ' + '|'+ ' ' + board[6])
    print('  ' + '|' + '   ' + '|')
    print('---------')
    print('  ' + '|' + '   ' + '|')
    print(board[1] + ' ' + '|'+ ' ' + board[2]+ ' ' + '|'+ ' ' + board[3])
    print('  ' + '|' + '   ' + '|')
    
    
#function that takes in a player input and assign their marker as 'X' or 'O'
def player_input():
    marker=input('Player 1:Do you want to be X or O')
    while marker!='X' and marker!='O':
        print('Choose from the valid options, X or O')
        marker=input('Do you want to be X or O')
    
    player1=marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return (player1,player2)


# function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    
        if position>=1 and position<=9:
            board[position]=marker
            

# function that takes in a board and a mark(X or O) and then checks to see if that mark has won or not
def win_check(board, mark):
    if (board[1]==board[4]==board[7]==mark or 
    board[2]==board[5]==board[8]== mark or 
    board[3]==board[6]==board[9]== mark or 
    board[1]==board[2]==board[3]== mark or 
    board[4]==board[5]==board[6]== mark or 
    board[7]==board[8]==board[9]== mark or 
    board[1]==board[5]==board[9]== mark or 
    board[3]==board[5]==board[7]== mark):
        return True
        
    else:
        return False


#function that randomly decide which player goes first
from random import randint
def choose_first():
    val=randint(0,1) 
    if val==0:
        print('Player 1 goes first')
        
    else:
        print('Player 2 goes first')
        
    return val  

 # function that checks whether a space on the board is freely available or not
def space_check(board, position):
    return board[position]==' '

# function that checks if the board is full or not
def full_board_check(board):
    for i in range(1,10):
        if board[i]==' ':
            return False
    return True

# asks for a player's next position (as a number 1-9) and checks if it's a free position
def player_choice(board):
    pos=int(input('Enter the next position'))
    
    return space_check(board,pos),pos


#function that asks the player if they want to play again
def replay():
    play_again=input('Do you want to play again: Y/N')
    if play_again=='Y':
        return True
    else:
        return False
                     

# main code
def play_game():
    board=[' ']*10
    pos1=0
    win_flag=0

    player1_marker,player2_marker=player_input()

    val_result=choose_first()
    if val_result==0:
        marker=player1_marker
    else:
        marker=player2_marker

    ready=input('Are you ready to play? Enter yes or no')
    if ready=='yes':
        flag=1

    while flag==1:
        full_board_check_result=full_board_check(board)

        while not(full_board_check_result):
            player_choice_result,pos1=player_choice(board)


            if player_choice_result:
                place_marker(board,marker,pos1)
                display_board(board)
                full_board_check_result=full_board_check(board)

                win_check_result=win_check(board,marker)
                if win_check_result==True:
                    if marker==player1_marker:
                        print('Congratulations, player 1 won!')
                        win_flag=1
                        flag=0
                        break


                    else:
                        print('Congratulations, player 2 won!')
                        win_flag=1
                        flag=0
                        break


                if marker=='X':
                    marker='O'
                else:
                    marker='X'
            else:  
                print('Position occupied')
                print(full_board_check_result)


        else:
            if win_flag!=1:
                print('It is a draw!')
                flag=0


        play_ag=replay()
        if play_ag==True:
            flag=1
            full_board_check_result==False
            board=[' ']*10
            pos1=0
            win_flag=0
            play_game()

        else:
            flag=0
            
# calling the play_game function
play_game()

        
        
