# Prints an empty grid at the beginning of the game.
#Creates a game loop where the program asks the user to enter the cell coordinates,
# analyzes the move for correctness and shows a grid with the changes if everything is okay.
#Ends the game when someone wins or there is a draw.
#You need to output the final result at the end of the game. Good luck!
win_places = [[0,3,6],[0,1,2],[1,4,7],[2,5,8],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]
move = 1
game, winner = [], []
win = 'no'

print("---------")
print(f'|  ', f' ', f'  |')
print(f'|  ', f' ', f'  |')
print(f'|  ', f' ', f'  |')
print("---------")

def grid(tics):
    print("---------")
    print(f'| {tics[0]}', f'{tics[1]}', f'{tics[2]} |')
    print(f'| {tics[3]}', f'{tics[4]}', f'{tics[5]} |')
    print(f'| {tics[6]}', f'{tics[7]}', f'{tics[8]} |')
    print("---------")

def check_x():
    if item[0] == 'X':
        global win
        win = 'yes'
        return print('X wins')
def check_y():
    if item[0] == 'O':
        global win
        win = 'yes'
        return print('O wins')

tics = "         "

# 036 012 147 258 345 678 048 246

while move < 10 and win == 'no':
    cell = input()
    match cell[0]:
        case '3':
            loc = 5 + int(cell[2])
        case '2':
            loc = 2 + int(cell[2])
        case '1':
            loc = 0 + int(cell[2]) - 1
    if cell[0] not in ('1','2','3') or cell[2] not in ('1','2','3'):
        try:
            t1, t2 = int(cell[0]), int(cell[2])
        except ValueError:
            print("You should enter numbers!")
        else:
            print("Coordinates should be from 1 to 3!")
    elif tics[loc] in ('X','O'):
        print("This cell is occupied!")
    else:
        if move % 2 != 0:
            xo = 'X'
        else:
            xo = 'O'
        tics = tics[:loc] + xo + tics[loc + 1:]
        grid(tics=tics)
        count_blank = len([elem for elem in tics if elem == ' '])
        for item in win_places:
            comp = []
            for place in item:
                comp.append(tics[place])
            game.append(comp)
            for item in game:
                if item[0] == item[1] == item[2]:
                    check_x()
                    check_y()
        if win == 'yes':
            break
        if count_blank == 0:
            print('Draw')
        move += 1

"""

        count_X = len([elem for elem in tics if elem == 'X'])
        count_O = len([elem for elem in tics if elem == 'O'])
if len(winner) > 1:
    print("Impossible")
elif len(winner) == 1:
    print(winner[0] + " wins")
else:
    pass

        if count_blank == 0 and len(winner) == 0:
            print("Draw")

if count_blank > 1 and len(winner) == 0:
    print('Game not finished')

if abs(count_X - count_O) > 1:
    print("Impossible")



| x x x |
| o o o |
 - - -
"""

"""if index_x in win_places or index_o in win_places:
    if index_x in win_places and index_o in win_places:
        print("Impossible")
    elif abs(count_X - count_O) > 1:
        print("Impossible")
    else:
        pass

indices_o = re.finditer(pattern='O', string=tics)
index_o = [index.start() for index in indices_o]
indices_x = re.finditer(pattern='X', string=tics)
index_x = [index.start() for index in indices_x]


else:
    print("Draw")"""


