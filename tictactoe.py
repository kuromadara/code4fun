import os
import itertools

def state_board(game_map, player = 0, row = 0, col = 0, just_display = False):

    try: 
        
        
        if(game_map[row][col]) == 0:

            game_map[row][col] = player

            header = "   " + "  ".join([str(x) for x in range(len(game_map))])
            
            print(header)
            
            for count, row in enumerate(board):
                print(count, row)
            global play_count
            play_count += 1

            #game_map[0] + game_map[1] + game_map[2]

            if(play_count-1 == len(game_map)**2):
                win_condition(game_map)
                if not win_condition:
                    print("Draw")
                
                restart()

            return game_map;
        
        else:
            
            current_player = next(player_cycle)
            
            print(header)
            for count, row in enumerate(board):
                print(count, row)
            print("This space is occupied")

            return game_map;

    except IndexError as e:
        print("Error: Row/ Column value must b 0-2", e)
    
    except Exception as e:
        print("Something went wrong", e)


def check_win(row):

    if row.count(row[0]) == len(row) and row[0] != 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Winner! is player {row[0]}")
        
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

    print(f"Do you want to play again? (y/n)")
    response = input()

    if(response == "y"):
        global play
        global game_won
        global board
        play = True
        game_won = False
        board = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
        state_board(board, just_display = True)
        player_cycle = itertools.cycle(players)     
    else:
        print("Thanks for playing")

              

play = True
game_won = False
players = [1, 2]
play_count = 0

# current_player = 2

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


state_board(board, just_display = True)
player_cycle = itertools.cycle(players)
while play:
    
    while game_won == False:
        current_player = next(player_cycle)
        print(f"Current Player is: {current_player}")
        row_choice    = int(input("Enter row choice (0,1,2): "))
        column_choice = int(input("Enter your column choice (0,1,2): "))

        os.system('cls' if os.name == 'nt' else 'clear')


        state = state_board(board, current_player, row_choice, column_choice)

        win_state = win_condition(state)

        if(win_state):
            play = False
            game_won = True

            restart()

            