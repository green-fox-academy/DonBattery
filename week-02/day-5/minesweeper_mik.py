from os import system # OS for clear the screen
import random # import this to get random numbers
from termcolor import cprint # this needs for the colors in the terminal (pip install termcolor)
import sys # we need this for the character codec setup
import codecs # also this is needed to set up the character codec

# The initial size of the minefield (it is allways square)
SIZE = 9

# The initial number of mines on the minefield
MINES = 9

# Allign the minefield a bit to the right
Indention = 20

# Assign colors to "numbers" (mine indexes on the field)
colors = ['white', 'blue', 'magenta', 'red', 'cyan', 'red', 'red', 'red', 'red']

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

# Draw out the grid
def draw(grid):
    clear_screen()
    print('\n')
    cprint('. o O o . o O o . o O o--=M i n e S w e e p e R=--o O o . o O o . o O o .', 'yellow')
    cprint('_    _   __   ___ ____|', 'yellow', end = '')
    for i in range(1, SIZE + 1):
        if i < 10:
            symbol = ' ' + str(i) + ' '
        else:
            symbol = str(i) + ' ' 
        cprint(symbol, 'green', end = '')
    cprint('|____ ___  __   _     _', 'yellow')   
    for y_cord in range(0, SIZE):
        if y_cord + 1 < 10:
            symbol = ' ' + str(y_cord + 1) + ' '
        else:
            symbol = str(y_cord + 1) + ' '
        cprint(Indention * ' ' + symbol, 'green', end ='')
        for x_cord in range(0, SIZE):
            if grid[x_cord][y_cord]['isMine'] and grid[x_cord][y_cord]['isChecked']:
                symbol = 'X'
                color = 'red'
            elif grid[x_cord][y_cord]['isChecked']:
                if grid[x_cord][y_cord]['number'] > 0:
                    color = colors[grid[x_cord][y_cord]['number']]
                    symbol = str(grid[x_cord][y_cord]['number'])
                else:
                    color = colors[0]
                    symbol = ' '
            else:
                color = 'white'
                symbol = '?'
            print('[', end = '')
            cprint(symbol, color, end = '')
            print(']', end='')
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

# Get player input (halts program on userinput Q or q)
def get_xy_cord():
    correct = False
    while not correct:
        Sinput = input(' ' * Indention + ' Field to check ? (X Y) 1 - ' + str(SIZE) + ' : ')
        if (len(Sinput) >=3 and Sinput.count(' ') == 1 and Sinput.find(' ') != 0 and Sinput.find(' ') != len(Sinput) - 1) or (Sinput in ['q', 'Q']):
            if Sinput not in ['q', 'Q']:
                x_cord, y_cord = Sinput.split()
                if x_cord.isnumeric() and y_cord.isnumeric():
                    x_cord, y_cord = int(x_cord), int(y_cord)
                    if 0 < x_cord <= SIZE and 0 < y_cord <= SIZE:
                        correct = True
            else:
                quit() # I know, I know....
    return x_cord - 1, y_cord - 1

# Check if the player has won the game
def won_situation(grid):
    already_checked = 0
    for x_cord in range(SIZE):
        for y_cord in range (SIZE):
            if grid[x_cord][y_cord]['isChecked']:
                already_checked += 1
    return already_checked == SIZE ** 2 - MINES

# Setup the character encode on the terminal
def set_encode():
    if sys.stdout.encoding != 'cp850':
        sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
    if sys.stderr.encoding != 'cp850':
        sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'strict')

# Initialize everything and enter into the main game loop (which end on won or lost condition)
def start_game():
    set_encode()
    grid = init_map(SIZE)
    init_mines(grid, MINES)
    init_numbers(grid)
    is_live = True
    won = False
    draw(grid)
    while is_live and not won:
        x_cord, y_cord = get_xy_cord()
        is_live = not check(grid, x_cord, y_cord)
        won = won_situation(grid)
        draw(grid)
    if won:
        cprint(' ' * Indention + ' You are a winner!', 'green')
    else:
        cprint(' ' * Indention + ' You just lost The Game!', 'red')

start_game()
