from game_function import *

initial_state()

while condition:
    is_end_game()
    print("##############################")
    print("Displaying commands:")
    print("What would you like to do?")
    print("F-flag,O-Open,Exit")
    print("")
    print("Enter coordinates in the format of x y F/O")
    user_input=input("Enter: ")
    condition=handle_input(user_input)
    print("")