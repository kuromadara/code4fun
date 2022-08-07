import os
import itertools

def state_board(game_map, player = 0, row = 0, col = 0, just_display = False):

    try: 
        
        header = "   " + "  ".join([str(x) for x in range(len(game_map))])

        if(game_map[row][col]) == 0:

            game_map[row][col] = player

            print(header)
            for count, row in enumerate(board):
                print(count, row)
            global play_count
            play_count += 1

            if(play_count-1 == len(game_map)**2):
                win_condition(game_map)
                if win_condition != True:
                    print("Draw")

                restart()

            return game_map;

        if(game_map[row][col] != 0):
            current_player = next(player_cycle)
            
            print(header)
            for count, row in enumerate(board):
                print(count, row)
            print("This space is occupied")

            return game_map;
        
        
        return False;
        
            

    except IndexError as e:
        print(f"Error: Row/Column value must be between (0-{board_size - 1})", e)
        current_player = next(player_cycle)
        return False;
    
    except Exception as e:
        print("Something went wrong", e)
        return False;


def check_win(row):

    if row.count(row[0]) == len(row) and row[0] != 0:
        # os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Winner! is player {row[0]}")
        global player_cycle
        player_cycle = itertools.cycle(players)     
        return True;

    return False;

def win_condition(current_board):

    #diagonal win

    diag = []

    for index in range(len(board)):
        diag.append(board[index][index])

    win = check_win(diag)

    if(win):
        return True;
    

    diag = []
    
    for col, row in enumerate(reversed(range(len(board)))):
        diag.append(board[row][col])

    

    win = check_win(diag)
    
    if(win):
        return True;
  
            
    #horizantal win

    for row in board:

        win = check_win(row)

        if(win):
            return True;
        

       

    #vertical win

    for col in range(len(board)):
         
        check = []

        for row in board:
            check.append(row[col])
            
        win = check_win(check)
        if(win):
            return True;
    
    return False;


def restart():

    global play_count
    play_count = 0
    print(f"Do you want to play again? (y/n)")
    response = input()

    if(response == "y"):
        global play
        global game_won
        global board
        global board_size
        play = True
        game_won = False
        board = [[0 for row in range(board_size)] for col in range(board_size)]
                 
        state_board(board, just_display = True)
        player_cycle = itertools.cycle(players)     
    else:
        print("Thanks for playing")

              

play = True
game_won = False
players = [1, 2]
play_count = 0

# os.system('cls' if os.name == 'nt' else 'clear')

board_size = int(input("Enter the size of the board: "))

if(board_size <=0):
    print("Board size must be greater than 0")
    play = False
    board_size = int(input("Enter the size of the board: "))


board = [[0 for row in range(board_size)] for col in range(board_size)]
play = True

state_board(board, just_display = True)
player_cycle = itertools.cycle(players)

while play:
    
    while game_won == False:
        current_player = next(player_cycle)
        print(f"Current Player is: {current_player}")
        row_choice    = int(input(f"Enter row choice between (0-{board_size-1}): "))
        column_choice = int(input(f"Enter your column choice (0-{board_size-1}): "))

        # os.system('cls' if os.name == 'nt' else 'clear')


        state = state_board(board, current_player, row_choice, column_choice)

        win_state = win_condition(state)

        if(win_state):
            play = False
            game_won = True

            restart()

            