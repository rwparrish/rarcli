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
            while True:
                manage_menu()
                manage_choice = input("> ")
                if manage_choice == "0":
                    main()
                elif manage_choice == "1":
                    new_game()
                elif manage_choice == "2": 
                    delete_game()
                elif manage_choice == "3":
                    new_review()
                # elif manage_choice == "4":
                #     # update_review()
                # elif manage_choice == "5":
                    # delete_review()
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
    print("2. Delete an existing game")
    print("3. Enter a new review for an existing game")
    print("4. Update a review for an existing game")
    print("5. Delete a review for an existing game")


if __name__ == "__main__":
    main()
