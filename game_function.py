import random
from blockclass import testblock

row=0
col=0
x=0
flags=0
correct_bomb_identified=0
existing = [] #check
condition=True #check

def difficulty(x):
    global row
    global col
    global bomb
    global correct_bomb_identified
    global display_bomb_identified
    if x == "Intro":
        bomb = 3
        col = 5
        row = 5
        display_bomb_identified = bomb
        return True
    if x == "Easy":
        bomb = 10
        col = 9
        row = 9
        display_bomb_identified = bomb
        return True
    elif x == "Medium":
        bomb = 40
        col = 16
        row = 16
        display_bomb_identified = bomb
        return True
    elif x == "Hard":
        bomb = 99
        col = 16
        row = 30
        display_bomb_identified = bomb
        return True
    else:
        print("Unknown input-difficulty")
        return False

def display(set):
    print("")
    print("Displaying Minesweeper:")
    print("Difficulty is",text1)
    print("Bombs remaining:", display_bomb_identified)

    for i in range(col):
        print("----", end='')
    print("\n")
    print("     ", end='')
    for i in range(col):
        if (i != col - 1):
            if i<10:
                print("[ " + str(i) + " ]", end='')
            else:
                print("[ " + str(i) + "]", end='')
        else:
            if i < 10:
                print("[ " + str(i) + " ]")
            else:
                print("[ " + str(i) + "]")

    for i in range(row):
        if i < 10:
            print("[ " + str(i) + " ]",end='')
        else:
            print("[ " + str(i) + "]",end='')

        for j in range(col):
            if (j != col - 1):
                print(" ",set[i][j], " ", end='')
            else:
                print(" ",set[i][j])

def generate_dataset():
    if (row != 0 and col != 0):
        dataset = [["·" for x in range(col)] for x in range(row)]
    return dataset

def generate_bombs():
    global bomb_set
    bomb_set = [[random.randint(0, row - 1), random.randint(0, col - 1)] for x in range(bomb)]

    # clear duplicates
    for i in range(len(bomb_set) - 1):
        for j in range(i + 1, len(bomb_set)):
            if bomb_set[i][0] == bomb_set[j][0] and bomb_set[i][1] == bomb_set[j][1]:
                while (bomb_set[i][0] == bomb_set[j][0] and bomb_set[i][1] == bomb_set[j][1]):
                    bomb_set[i] = [random.randint(0, row - 1), random.randint(0, col - 1)]

    for y in range(bomb):
        dataset[bomb_set[y][0]][bomb_set[y][1]] = "X"

def onclick(x, y):
    # print("Testcase before:",testcase)#remove this
    if (x > row - 1 or x < 0 or y > col - 1 or y < 0):
        print("Unknown Coordinates")
        return ("error")
    elif dataset[y][x] == "X":
        print("Bomb!")
        end_game(False)
        condition = False
    else:
        global a
        a = testblock(x, y, dataset)
        neighbour(x, y)

def show_bombs(bomb_sets):
    for i in bomb_sets:
        displayset[i[0]][i[1]] = "X"

def flag(x, y):
    global flags
    global correct_bomb_identified
    global display_bomb_identified
    flags += 1
    displayset[y][x] = "F"
    display_bomb_identified -= 1
    if dataset[y][x] == "X":
        correct_bomb_identified += 1

def neighbour(x, y):
    global existing

    if [x, y] not in existing:
        existing.append([x, y])
        temp = testblock(x, y, dataset)

        if temp.bomb_number() == 0:
            # dataset[y][x] = " "
            displayset[y][x] = " "

            surround = temp.field_selector()
            for j in surround:
                neighbour(j[0], j[1])
        if temp.bomb_number() != 0:
            displayset[y][x] = temp.bomb_number()

        del temp

def handle_input(text):
    if text == "Exit":
        return False
    try:
        x, y, action = text.split()

        try:
            x = int(x)
            y = int(y)
            action = str(action)
        except:
            print("Unknown input, please try again")
            return True

        if (isinstance(x, int) and isinstance(y, int) and isinstance(action, str)):
            if action == "O":
                onclick(x, y)
                display(displayset)
            elif action == "F":
                flag(x, y)
                display(displayset)
            else:
                print("Unknown action")
            return True
        else:
            print("Unknown input, please try again")
            return True
    except (IndexError, ValueError):
        print("Unknown input, please try again")
        return True

def is_end_game():
    if correct_bomb_identified==bomb:
        end_game(True)

def end_game(result):
    if result:
        print("")
        print("##############################")
        print("Congratulations!")
        print("__   _____  _   _  __        _____ _   _ _ _ ")
        print("\ \ / / _ \| | | | \ \      / |_ _| \ | | | |")
        print(" \ V | | | | | | |  \ \ /\ / / | ||  \| | | |")
        print("  | || |_| | |_| |   \ V  V /  | || |\  |_|_|")
        print("  |_| \___/ \___/     \_/\_/  |___|_| \_(_(_)")
        exit()
    else:
        print("")
        print("##############################")
        print("Sorry you lost")
        print(bomb, "bomb(s) remaining")
        print("You added", flags, "flag(s)")
        print("You correctly identified", correct_bomb_identified, "bomb(s)")
        print("")
        for y in range(bomb):
            displayset[bomb_set[y][0]][bomb_set[y][1]] = "X"
        display(displayset)
        exit()

def initial_state():
    print("Please select difficulty - Intro, Easy, Medium, Hard")

    temp3 = False
    global text1
    while not temp3:
        text1=input("Enter difficulty: ")
        temp3 = difficulty(text1)

    global displayset
    global dataset
    displayset = generate_dataset()
    dataset = generate_dataset()
    generate_bombs()
    display(displayset)