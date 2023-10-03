# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    breakpoint()
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")
    print("2. Some useless Function")
    print("3. Some other nonsense")
    print("4. Pancakes")

if __name__ == "__main__":
    main()
