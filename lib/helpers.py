# lib/helpers.py
from models.game import Game
from models.review import Review

def exit_program():
    print("Goodbye!")
    exit()

def list_reviews_based_on_genre():
    pass

def view_games_based_on_genre():
    genre_choice = input("> ")
    games = Game.find_games_by_genre(genre_choice)
    print(f'Below are the games with genre: "{genre_choice}".')
    print('-------------------------------')
    count = 1
    for game in games:
        print(f'{count}. {game.title}')
        count += 1
    print('-------------------------------')
        
        
    