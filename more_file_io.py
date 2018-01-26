
import os
import random

path = "data"

file_names = os.listdir(path)

for i, f in enumerate(file_names):
    print(str(i + 1) + "), " + f)

choice = input('pick one: ')
choice = int(choice) - 1
print()

file = path + "/" + file_names[choice]
print(file)

with open(file, 'r') as f:
    lines = f.read().splitlines()

pass print(lines)

category_name = lines[0]
puzzle = random.choice( lines[1:] )

print(category_name)
print(puzzle)


def play():
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved)

    strikes = 0
    limit = 6

    while solved != puzzle:
        letter = get_guess()

        if letter not in puzzle:
            strikes += 1

        guesses += letter
        solved = get solved(puzzle, guesses)
        display_board(solved)
        print("")
        print ("strikes: " + str(strikes))
        print ("guesses: " + "(" + str(guesses) + ")")
        guesses += str(",")
        print ("")
        print ("")
        if strikes >= limit:
            show_result(puzzle, solved)
    show_result(puzzle, solved)
