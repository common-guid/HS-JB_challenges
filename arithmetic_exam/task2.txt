"""Generate a math task that looks like a math operation. Use the requirements above. Print it.
Read the answer from a user.
Check whether the answer is correct. Print Right! or Wrong!
"""

import random

place1 = random.randint(1,9)
place2 = random.randint(1,9)

if place1 in (1,2,3):
    op = '+'
elif place1 in (4,5,6):
    op = '-'
else:
    op = '*'

print(str(place1)+" "+op+" " +str(place2))
eq = str(place1) + op + str(place2)
total = eval(eq)

user = input()

if str(total) == user:
    print("Right!")
else:
    print("Wrong!")

