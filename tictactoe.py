from IPython.display import clear_output
import random

#FUNC RESPONSIBLE FOR DISPLAYING THE BOARD
def display_board(board):
    clear_output()
    print('     |     |     ')
    print('  '+board[7]+'  |  '+board[8]+'  |  '+board[9]+'  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print('  '+board[4]+'  |  '+board[5]+'  |  '+board[6]+'  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print('  '+board[1]+'  |  '+board[2]+'  |  '+board[3]+'  ')
    print('     |     |     ')

#ASSIGN MARKERS TO THE PLAYERS
def player_input():
    player1 = ''
    #KEEP ASKING P1 TO WRITE X OR O
    while player1 != 'X' and player1 != 'O':
        player1 = input('Player 1 - choose your marker: X or O? ')

    #ASSIGN P2
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return(player1,player2)

#CHOOSE THE FIRST PLAYER
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    
#CHOOSE YOUR POSITION (CHECK IF IT'S FREE)
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your position. Number 1-9 (numpad order): '))
        
    return position

#PLACE PLAYER'S MARKER ON THE BOARD
def place_marker(board, marker, position):
    board[position] = marker

#CHECK IF THE PLACE IS FREE
def space_check(board, position):
    return board[position] == ' '
    
#CHECK IF THE PLAYER HAS WON
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark))

#CHECK IF THE BOARD IS FULL
def full_board_check(board):
    return board.count('O') + board.count('X') == 9

#DO YOU WANT TO PLAY AGAIN?
def replay():
    decision = input('Do you want to play again? Yes or No? ')
    if decision.lower()[0] == 'y':
        return True
    else:
        return False
    
'''
TIC TAC TOE STARTS HERE
'''

print('Welcome to Tic Tac Toe!')

while True:
    #RESET THE BOARD
    game_board = [' '] * 10
    #CHOOSE YOUR MARKERS
    player1_marker, player2_marker = player_input()
    #DECIDE AND INFORM WHO GOES FIRST
    turn = choose_first()
    print(turn + ' will start!')
    
    #ARE YOU READY?
    play_game = input('Are you ready to play? Yes or No.')
    if play_game.lower()[0] == 'y':
        game_active = True
    else:
        game_active = False
    
    while game_active:
        if turn == 'Player 1':
        #PLAYER_1 LOGIC (DISPLAY THE BOARD, CHOOSE POSITION, PLACE THE MARKER)
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player1_marker, position)
        
            #CHECK IF PLAYER_1 WON
            if win_check(game_board, player1_marker):
                display_board(game_board)
                print('Congratulations Player 1! You have won the game!')
                game_active = False
            else:
                if full_board_check(game_board):
                    print('Draw!')
                    break
                else:
                    turn = 'Player 2'            
        
        else:
        #PLAYER_2 LOGIC (DISPLAY THE BOARD, CHOOSE POSITION, PLACE THE MARKER)
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player2_marker, position)
        
            #CHECK IF PLAYER_2 WON
            if win_check(game_board, player2_marker):
                display_board(game_board)
                print('Congratulations Player 2! You have won the game!')
                game_active = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('Draw!')
                    break
                else:
                    turn = 'Player 1'  

    if not replay():
        print('Thank you for playing Tic Tac Toe.')
        break