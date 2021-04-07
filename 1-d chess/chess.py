###
### Author: Sornali Rahman.
### Description: This program implements a 1D chess game. It takes user input
###              to find position and moves for White and Black and plays a chess game
###

from graphics import graphics

W_KNIGHT = 'WKn'
W_KING   = 'WKi'
B_KNIGHT = 'BKn'
B_KING   = 'BKi'
EMPTY    = '   '
WHITE    = 'White'
BLACK    = 'Black'
LEFT     = 'l'
RIGHT    = 'r'

def is_valid_move(board, position, player):
    ''' Implement. '''
    result = False
    if position <= 9:
        result=True
    return result



def move_knight(board, position, direction):
    ''' Implement. '''


def move_king(board, position, direction):
    ''' Implement. '''
    piece = board[position]
    board[position] == EMPTY
    if direction == LEFT:
        board[position - 1] = piece
    else:
        board[position + 1] = piece

def print_board(board):

    print('+-----------------------------------------------------+')
    print('|', end = "")
    for i in board:
        if i == EMPTY:
            print(' '+i+' |', end = "")
        else:
            print(' '+i+' |', end = "")
    print('\n+-----------------------------------------------------+')

def draw_board(board, gui):
    ''' Implement. '''

def is_game_over(board):
    ''' Implement. '''
    if (W_KING in board and B_KING in board):
        return False
    elif W_KING in board:
        print_board(board)
        print('White wins!')
        return True
    else:
        print_board(board)
        print('Black wins!')
        return True

def move(board, position, direction):
    ''' Implement. '''
    piece = board[position]
    if piece == W_KNIGHT or piece == B_KNIGHT:
        move_knight(board, position, direction)
    else:
        move_king(board, position, direction)

def main():

    # Create the canvas
    gui = graphics(700, 200, '1 Dimensional Chess')

    # This is the starting board.
    # This board variable can and should be passed to other functions
    # and changed as moves are made.
    board = [W_KING, W_KNIGHT, W_KNIGHT, EMPTY, EMPTY, EMPTY, B_KNIGHT, B_KNIGHT, B_KING]

    # White typically starts in chess.
    # This will change between WHITE and BLACK as the turns progress.
    player = WHITE

    # This variable will be updated to be True if the game is over.
    # The game is over after one of the kings dies.
    is_game_won = False

    # This loop controls the repetitive nature of the turns of the game.
    while not is_game_won:

        print_board(board)

        # Draw the board
        draw_board(board, gui)

        position = int(input(player + ' enter index:\n'))
        direction = input(player + ' enter direction (l or r):\n')

        # If the desired move is valid, then call the move function.
        # Also, change the player variable.
        if is_valid_move(board, position, player):
            if player == WHITE:
                move(board, position, direction)
                player = BLACK
            else:
                move(board, position, direction)
                player = WHITE
            # Draw the board again
            draw_board(board, gui)
            is_game_won = is_game_over(board)

main()
