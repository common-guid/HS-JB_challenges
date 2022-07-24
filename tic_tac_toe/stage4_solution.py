#Get the initial 3x3 grid from the input as in the previous stages. Here the user should input 9 symbols representing the field,
# for example, _XXOO_OX_.
#Output this 3x3 grid as in the previous stages.
#Prompt the user to make a move. The user should input 2 coordinate numbers that represent the cell
# where they want to place their X, for example, 1 1.
#Analyze user input. If the input is incorrect, inform the user why their input is wrong:
#   Print This cell is occupied! Choose another one! if the cell is not empty.
#   Print You should enter numbers! if the user enters non-numeric symbols in the coordinates input.
#   Print Coordinates should be from 1 to 3! if the user enters coordinates outside the game grid.
#Keep prompting the user to enter the coordinates until the user input is valid.
#If the input is correct, update the grid to include the user's move and print the updated grid to the console.

def grid(tics):
    print("---------")
    print(f'| {tics[0]}', f'{tics[1]}', f'{tics[2]} |')
    print(f'| {tics[3]}', f'{tics[4]}', f'{tics[5]} |')
    print(f'| {tics[6]}', f'{tics[7]}', f'{tics[8]} |')
    print("---------")

tics = input()
grid(tics=tics)
    # 036 012 147 258 345 678 048 246
move = 'yes'
while move == 'yes':
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
        tics = tics[:loc] + 'X' + tics[loc + 1:]
        grid(tics=tics)
        break