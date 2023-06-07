#Andres Portillo
#3/1/2023
#COP3502



#Andres Portillo
#3/1/2023
#COP3502


# Define the dimensions of the board
height = int(input('What would you like the height of the board to be?'))
length = int(input('What would you like the length of the board to be?'))

# Initialize the board to all empty cells
board = [['-' for j in range(length)] for i in range(height)]

# Initialize the players
current_player = 0
players = ['x', 'o']
print_players = True

# Define a function to print the board
def print_board():
    for row in board:
        print(' '.join(row))
    print('')


# Start the game loop
while True:
    # Print the current board state
    print_board()

    if print_players:
        print(f"Player 1: x\nPlayer 2: o")
        print_players = False
    # Get the current player's move
    print()
    while True:
        try:
            col = int(input(f'Player {current_player + 1}: Which column would you like to choose?'))
            if not 0 <= col < length:
                print(f'Column {col} is not valid. Please choose a column between 0 and {length - 1}.')
            elif board[0][col] != '-':
                print(f'Column {col} is already full. Please choose another column.')
            else:
                break
        except ValueError:
            print('Please enter a valid integer.')

    # Place the current player's piece in the chosen column
    row = height - 1
    while row >= 0:
        if board[row][col] == '-':
            board[row][col] = players[current_player]
            break
        row -= 1

    # Check for a win
    for i in range(height):
        for j in range(length):
            for di, dj in [(0, 1), (1, 0), (1, 1), (-1, 1)]:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= height or nj < 0 or nj >= length:
                    continue
                if board[i][j] != '-' and board[i][j] == board[ni][nj]:
                    ni, nj = ni + di, nj + dj
                    if ni < 0 or ni >= height or nj < 0 or nj >= length:
                        continue
                    if board[i][j] == board[ni][nj]:
                        ni, nj = ni + di, nj + dj
                        if ni < 0 or ni >= height or nj < 0 or nj >= length:
                            continue
                        if board[i][j] == board[ni][nj]:
                            print_board()
                            print(f'Player {current_player + 1} won the game!')
                            exit()

    # Check for a tie
    if all(cell != '-' for row in board for cell in row):
        print_board()
        print('Draw. Nobody wins.')
        exit()

    # Switch to the other player
    current_player = (current_player + 1) % 2

