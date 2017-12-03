from os import system # OS for clear the screen
import random # import this to get random numbers

# The initial size of the minefield (it is allways square)
SIZE = 9

# The initial number of mines on the minefield
MINES = 9

# Allign the minefield a bit to the right
Indention = 20

# Initialize the minefield as a matrix (list within list) of dictionaries containing the attributes of the individual fields
def init_map(size):
    return [[{'isMine': False, 'isChecked': False, 'number': 0} for _ in range(size)] for _ in range(size)]

# Fill the minefield randomly, with max_number mines
def init_mines(grid, max_mines):
    for _ in range(max_mines):
        mine_x_cord = random.randint(0, SIZE - 1)
        mine_y_cord = random.randint(0, SIZE - 1) 
        while grid[mine_x_cord][mine_y_cord]['isMine']: # We do not want to place mines to positions where ther are already one
            mine_x_cord = random.randint(0, SIZE - 1)   # So re-roll mine_x_cord, mine_y_cord until we find an empty place
            mine_y_cord = random.randint(0, SIZE - 1)
        grid[mine_x_cord][mine_y_cord]['isMine'] = True

# Inicializing the 'numbers' attribute on the grid, indicating the number of mines nearby
def init_numbers(grid):
    for x_cord in range(0, SIZE):
        for y_cord in range(0, SIZE):
            if grid[x_cord][y_cord]['isMine']:
                for x_check in range(-1, 2):
                    for y_check in range(-1, 2):
                        if -1 < x_cord + x_check < SIZE and -1 < y_cord + y_check < SIZE:
                            grid[x_cord + x_check][y_cord + y_check]['number'] += 1

# Clear the screen
def clear_screen():
    system('clear')

# Drow out the grid
def draw(grid):
    clear_screen()
    print('\n')
    print('¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸- =M i n e S w e e p e R= -¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸')
    print('        ¸,ø¤°º¤ø,¸. o O', end ='')
    for i in range(1, SIZE + 1):
        if i < 10:
            symbol = ' ' + str(i) + ' '
        else:
            symbol = str(i) + ' ' 
        print(symbol, end = '')
    print('O o .¸,ø¤°º¤ø,¸ ¸')   
    for y_cord in range(0, SIZE):
        if y_cord + 1 < 10:
            symbol = ' ' + str(y_cord + 1) + ' '
        else:
            symbol = str(y_cord + 1) + ' '
        print(Indention * ' ' + symbol, end ='')
        for x_cord in range(0, SIZE):
            if grid[x_cord][y_cord]['isMine'] and grid[x_cord][y_cord]['isChecked']:
                symbol = 'X'
            elif grid[x_cord][y_cord]['isChecked']:
                if grid[x_cord][y_cord]['number'] > 0:
                    symbol = str(grid[x_cord][y_cord]['number'])
                else:
                    symbol = ' '
            else:
                symbol = '?'
            print('[' + symbol + ']', end='')
        print('\n')

# Recursive algorithm to discover numbers around a given field (if it finds a zero it calls itself on that position)
def discover(grid, x_cord, y_cord):
    for x_check in range(-1, 2):
        for y_check in range(-1, 2):            
            if -1 < x_cord + x_check < SIZE and -1 < y_cord + y_check < SIZE:
                if not grid[x_cord + x_check][y_cord + y_check]['isChecked']:
                    grid[x_cord + x_check][y_cord + y_check]['isChecked'] = True
                    if grid[x_cord + x_check][y_cord + y_check]['number'] == 0:
                        discover(grid, x_cord + x_check, y_cord + y_check)

# Check a coordinate given by the player. Returns true if player stepped on mine. Starts to discover if player stepped on zero
def check(grid, x_cord, y_cord):    
    grid[x_cord][y_cord]['isChecked'] = True
    if grid[x_cord][y_cord]['isMine']:
        return True
    elif grid[x_cord][y_cord]['number'] == 0:
        discover(grid, x_cord, y_cord)
    return False

# Get player input (needs finetuning)
def get_row_and_col(grid):
    input_string = input(' ' * Indention + 'Which field to check ? (X Y) 1 - ' + str(SIZE) + ' : ')    
    x_cord, y_cord = input_string.split()
    x_cord, y_cord = int(x_cord) - 1, int(y_cord) - 1    
    return x_cord, y_cord

# Check if the player has won the game
def won_situation(grid):
    already_checked = 0
    for x_cord in range(SIZE):
        for y_cord in range (SIZE):
            if grid[x_cord][y_cord]['isChecked']:
                already_checked += 1
    return already_checked == SIZE ** 2 - MINES

# Initialize everything and enter into the main game loop (which end on won or lost condition)
def start_game(): 
    grid = init_map(SIZE)
    init_mines(grid, MINES)
    init_numbers(grid)
    is_live = True
    won = False
    draw(grid)
    while is_live and not won:
        x_cord, y_cord = get_row_and_col(grid)
        is_live = not check(grid, x_cord, y_cord)
        won = won_situation(grid)
        draw(grid)
    if won:
        print('You are a winner!')
    else:
        print('You just lost The Game!')

start_game()
