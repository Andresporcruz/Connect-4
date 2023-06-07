def print_board(board):
    for row in board:
        print(' '.join(row))
    print('')

def initialize_board(height, length):
    board = [['-' for j in range(length)] for i in range(height)]
    return board

def insert_chip(board, col, chip_type):
    for row in range(height-1, -1, -1):
        if board[row][col] == '-':
            board[row][col] = chip_type
            return row

    # if the column is full, return -1 to indicate an error
    return -1

def check_if_winner(board, col, row, chip_type):
    # check horizontal
    if col >= 3 and all(cell == chip_type for cell in board[row][col-3:col]):
        return True
    if col <= length-4 and all(cell == chip_type for cell in board[row][col:col+4]):
        return True

    # check vertical
    if row >= 3 and all(board[row-i][col] == chip_type for i in range(4)):
        return True

    # check diagonal \
    if col >= 3 and row >= 3 and all(board[row-i][col-i] == chip_type for i in range(4)):
        return True
    if col <= length-4 and row <= height-4 and all(board[row+i][col+i] == chip_type for i in range(4)):
        return True

    # check diagonal /
    if col >= 3 and row <= height-4 and all(board[row+i][col-i] == chip_type for i in range(4)):
        return True
    if col <= length-4 and row >= 3 and all(board[row-i][col+i] == chip_type for i in range(4)):
        return True

    return False


# Define the dimensions of the board
height = int(input('What would you like the height of the board to be? '))
length = int(input('What would you like the length of the board to be? '))

# Initialize the board to all empty cells
board = initialize_board(height, length)

# Initialize the players
current_player = 0
players = ['x', 'o']
print_players = True

# Start the game loop
while True:
    # Print the current board state
    print_board(board)

    if print_players:
        print(f"Player 1: x\nPlayer 2: o")
        print_players = False

    # Get the current player's move
    print()
    while True:
        try:
            col = int(input(f'Player {current_player + 1}: Which column would you like to choose? '))
            if not 0 <= col < length:
                print(f'Column {col} is not valid. Please choose a column between 0 and {length - 1}.')
            elif board[0][col] != '-':
                print(f'Column {col} is already full. Please choose another column.')
            else:
                break
        except ValueError:
            print('Please enter a valid integer.')

    # Place the current player's piece in the chosen column
    row = insert_chip(board, col, players[current_player])

    # Check for a win
    if check_if_winner(board, col, row, players[current_player]):
        print_board(board)
        print(f'Player {current_player + 1} won the game!')
        exit()

    # Check for a tie
    if all(cell != '-' for row in board for cell in row):
        print_board(board)

    current_player = (current_player + 1) % 2