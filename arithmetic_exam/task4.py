"""
With the first message, the program should ask for a difficulty level:
1 - simple operations with numbers 2-9
2 - integral squares 11-29

A user enters an answer.
For the first difficulty level: the task is a simple math operation; the answer is the result of the operation.
For the second difficulty level: the task is an integer; the answer is the square of this number.
In case of another input: ask to re-enter. Repeat until the format is correct.

The application gives 5 tasks to a user.

The user receives one task, prints the answer.
If the answer contains a typo, print Incorrect format. and ask to re-enter the answer. Repeat until the answer is in the correct format.
If the answer is a number, print Right! or Wrong! Go to the next question.

After five answers, print Your mark is N/5. where N is the number of correct answers.

Output Would you like to save your result to the file? Enter yes or no.
In case of yes, YES, y, Yes: the app should ask the username and write Name: n/5 in level X (<level description>).
    (X stands for the level number) in the results.txt file. For example — Alex: 3/5 in level 1 (simple operations with numbers 2-9).
The results should be saved to the file immediately after the user gave the positive answer to the question Would you
    like to save your result to the file?
If the file results.txt does not exist, you should create it.

In case of no or any other word: exit the program.
"""
import random

msg1 = "Which level do you want? Enter a number: "
msg2 = "1 - simple operations with numbers 2-9"
msg3 = "2 - integral squares of 11-29"

def level():
    print(msg1)
    print(msg2)
    print(msg3)
    level = input()
    return level

def opt1():
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

def opt2():
    place3 = random.randint(11,29)
    print(place3)
    total = place3 ** 2
    return total

def check1():
    right = 0
    for i in range(5):
        again = 'y'
        total = opt1()
        user = input()
        while again == 'y':
            try:
                int(user)
                if str(total) == str(user):
                    print("Right!")
                    right += 1
                    again = 'n'
                else:
                    print("Wrong!")
                    again = 'n'
            except:
                print("Incorrect format")
                user = input()
    return right

def check2():
    right = 0
    for i in range(5):
        again = 'y'
        total = opt2()
        user = input()
        while again == 'y':
            try:
                int(user)
                if str(total) == str(user):
                    print("Right!")
                    right += 1
                    again = 'n'
                else:
                    print("Wrong!")
                    again = 'n'
            except:
                print("Incorrect format")
                user = input()
    return right

forward = 0

while forward == 0:
    level = level()
    if level not in ('1','2'):
        continue
    else:
        forward = 1

if level == '1':
    description = "(simple operations with numbers 2-9)."
    right = check1()
if level == '2':
    description = "(integral squares of 11-29)."
    right=check2()

save = input("Your mark is " + str(right) +"/5. Would you like to save the result? "
                               "Enter yes or no.")
if save in ('y', 'Y', 'YES', 'Yes', 'yes'):
    name = input("what is your name?")
    f = open("results.txt", "a")
    f.write(name + ": " + str(right) +"/5 in level " + str(level) +" " + description)
    f.close()
    print('The results are saved in "results.txt".')