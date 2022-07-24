"""
The application should give the user 5 tasks. The tasks are akin to the previous stage: two numbers from
    2 to 9 and an integer operation.
The user receives one task, prints the answer. If the answer contains a typo (letters or otherwise empty),
    the program should print Incorrect format. and ask to re-enter the answer. Repeat until the answer is in the correct format.
    If the answer is a number, print Right! or Wrong! depending on the answer and carry on to the next question.
After five tasks, output Your mark is n/5. where n is the number of correct answers.
"""
import random

def gen_num():
    place1 = random.randint(2,9)
    place2 = random.randint(2,9)

    if place1 in (1,2,3):
        op = '+'
    elif place1 in (4,5,6):
        op = '-'
    else:
        op = '*'
    print(str(place1)+" "+op+" " +str(place2))
    eq = str(place1) + op + str(place2)
    total = eval(eq)
    return total

right = 0
wrong = 5

for i in range(5):
    again = 'y'
    total=gen_num()
    user = input()
    while again == 'y':
        try:
            int(user)
            if str(total) == str(user):
                print("Right!")
                right+=1
                again = 'n'
            else:
                print("Wrong!")
                again='n'
        except:
            print("Incorrect format")
            user=input()

print("Your mark is "+ str(right)+"/"+str(wrong))