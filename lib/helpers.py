# lib/helpers.py
from models.game import Game
from models.review import Review

import ipdb

def exit_program():
    print("Goodbye!")
    exit()

def view_games_alpha():
    games = Game.get_all()
    games.sort(key=lambda game: game.title)
    print("Games listed in Alphabetical Order:")
    print('-------------------------------')
    list_games(games)
    
def new_game():
    title = input("Enter the title of the game: ")
    year = input("Enter the year of the game: ")
    genre = input("Enter the genre of the game: ")
    multi = int(input("Enter '1' for yes and '0' for no: "))
    description = input("Enter a game description (10 - 50 characters): ")
    new_game = Game(title, year, genre, multi, description)
    new_game.save()
    print("Game successfully added.")
    input("Press enter to display list of games.")
    view_games_alpha()
    

def delete_game():
    print("Please select the game you wish to delete:")
    view_games_by_id()
    game_id = int(input("> "))
    game =  Game.all.get(game_id)
    user_input = input(f"Are you sure you would like to delete {game.title}? Enter 'y' or 'n'. ")
    # print(f"Are you sure you would like to delete {game.title}?")  
    if user_input == "y":
        game.delete()
        print("Game has been deleted.")
    elif user_input == "n":
        delete_game()
        
        

    
def view_games_by_id():
    games = Game.get_all()
    games.sort(key=lambda game: game.id)
    print('-------------------------------')
    list_games(games)


def view_games_based_on_genre():
    print("Please enter genre:")
    genre_choice = input("> ")
    games = Game.find_games_by_genre(genre_choice)
    print(f'Below are the games with genre: "{genre_choice}".')
    print('-------------------------------')
    list_games(games)
        

def view_games_based_on_avg_rating():
    games = Game.get_all()
    games_with_avg_rating = []
    for game in games:
        game.average_rating = average_rating(game.reviews())
        games_with_avg_rating.append(game)
    games_sorted_by_avg_rating = sorted(games_with_avg_rating, key=lambda game: game.average_rating, reverse=True)
    print("Games listed by Average Rating:")
    print('-------------------------------')
    count = 1
    for game in games_sorted_by_avg_rating:
        print(f'{count}. {game.title} - {game.average_rating}')
        count += 1
    print('-------------------------------')


def list_reviews_based_on_genre():
    print("Please enter genre:")
    genre_choice = input("> ")
    games = Game.find_games_by_genre(genre_choice)
    for game in games:
        print(f'Reviews for {game.title}')
        list_reviews(game.reviews())


def list_games(games):
    count = 1
    for game in games:
        print(f'{count}. {game.title}')
        count += 1
    print('-------------------------------')
    
    
def list_reviews(reviews):
    count = 1
    for review in reviews:
        print(f'{count}. {review.header} - {review.rating} - {review.content}')
        count += 1
    print('-------------------------------')


def average_rating(reviews):
    ratings = [review.rating for review in reviews]
    total_ratings = sum(ratings)
    average_rating = total_ratings / len(ratings)
    return round(average_rating, 2)