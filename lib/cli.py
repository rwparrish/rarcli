# lib/cli.py
from helpers import *


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            while True:
                browse_menu() #browse_menu_control_flow
                browse_choice = input("> ")
                if browse_choice == "0":
                    main()
                elif browse_choice == "1":
                    view_games_alpha()
                elif browse_choice == "2":
                    view_games_based_on_genre()
                elif browse_choice == "3":
                    view_games_based_on_avg_rating()
                elif browse_choice == "4":
                    list_reviews_based_on_genre()
        elif choice == "2":
            manage_menu()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print('-------------------------------')
    print("0. Exit the program")
    print("1. Browse")
    print("2. Manage")

def browse_menu():
    print("Please select an option:")
    print('-------------------------------')
    print("0. Return to previous menu")
    print("1. View games in alphabetical order")
    print("2. View games based on genre")
    print("3. Views games based on average rating")
    print("4. List reviews based on genre")
       
def manage_menu():
    print("Please select an option:")
    print('-------------------------------')
    print("0. Return to previous menu")
    print("1. Enter a new game")
    print("2. Update an existing game")
    print("3. Enter a new review for an existing game")
    print("4. Display reviews for an existing game")

def reviews_menu(): #list all reviews for the game entered in line 54 above
    print("Please select an option:")
    print('-------------------------------')
    print("0. Return to previous menu")
    print("1. Enter a review number to update")
    print("2. Enter a review number to delete")

if __name__ == "__main__":
    main()
