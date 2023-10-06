# lib/cli.py
from helpers import *


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            browse_menu()
            browse_choice = input("> ")
            if browse_choice == "0":
                main()
            elif browse_choice == "1":
                view_games_based_on_genre()
        elif choice == "2":
            manage_menu()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Browse")
    print("2. Manage")

def browse_menu():
    print("0. Return to previous menu")
    print("1. List reviews based on genre")
    print("2. View games based on genre")
    print("3. View games in alphabetical order")
    print("4. Views games based on average ratings game")
       
def manage_menu():
    breakpoint()
    print("0. Return to previous menu")
    print("1. Browse")
    print("2. Manage")

if __name__ == "__main__":
    main()
