import re
tics = input("Enter cells: ")

print("---------")
print(f'| {tics[0]}', f'{tics[1]}', f'{tics[2]} |')
print(f'| {tics[3]}', f'{tics[4]}', f'{tics[5]} |')
print(f'| {tics[6]}', f'{tics[7]}', f'{tics[8]} |')
print("---------")

    # 036 012 147 258 345 678 048 246

win_places = [[0,3,6],[0,1,2],[1,4,7],[2,5,8],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]
indices_o = re.finditer(pattern='O', string=tics)
index_o = [index.start() for index in indices_o]
indices_x = re.finditer(pattern='X', string=tics)
index_x = [index.start() for index in indices_x]
count_X = len([elem for elem in tics if elem == 'X'])
count_O = len([elem for elem in tics if elem == 'O'])
count_blank = len([elem for elem in tics if elem == '_'])
# Impossible when the grid has three X's in a row as well as three O's in a row,
# or there are a lot more X's than O's or vice versa (the difference should be 1 or 0;
# if the difference is 2 or more, then the game state is impossible).
game, winner = [], []
i = 0
for item in win_places:
    comp = []
    for place in item:
        comp.append(tics[place])
    game.append(comp)
    i += 1

for item in game:
    if len(set(item)) == 1:
        winner.append(str(item)[2])

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