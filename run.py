from tictactoe import *

playing_board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

print("""
———————————————————————————————————
Welcome to TicTacToe against an AI.
———————————————————————————————————
""")

playing = int(input(
    """If you want to play yourself press: 1 

If you want to see two AI's play against each other, press: 2

_"""))
print_board(playing_board)

if playing == 1:
    print("""
You will be playing "X" while the AI will be "O".

Please select a field on the numerically marked board.  
""")

    while not game_is_over(playing_board):
        player_move = int(input('Choose a field to place your "X":'))
        select_space(playing_board, player_move, "X")
        print_board(playing_board)
        if not game_is_over(playing_board):
            select_space(playing_board, minimax(playing_board, False)[1], "O")
            print_board(playing_board)

    winner = evaluate_board(playing_board)
    if winner == 1:
        print('You have won congratulations!')
    elif winner == -1:
        print('You lost.. better luck next time!')
    else:
        print("It's a tie!! Run the script again to play again. ")

elif playing == 2:

    print("Cool. Here is the game of two AI's against each other:")

    while not game_is_over(playing_board):
        select_space(playing_board, minimax(playing_board, True)[1], "X")
        print_board(playing_board)
        if not game_is_over(playing_board):
            select_space(playing_board, minimax(playing_board, False)[1], "O")
            print_board(playing_board)

else:
    raise ValueError("Sorry, this option is not available.")
