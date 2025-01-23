# lib/helpers.py

from models.game import Game
from models.review import Review
from cli  import manage_menu
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
    multi = int(input("Is this game multiplayer? '1' for yes and '0' for no: "))
    description = input("Enter a game description (10 - 50 characters): ")
    new_game = Game(title, year, genre, multi, description)
    new_game.save()
    print("Game successfully added.")
    input("Press enter to display list of games.")
    view_games_alpha()
    

def delete_game():
    print("Please select the game you wish to delete:")
    view_games_by_id()
    user_choice = int(input("> "))
    if user_choice == 0:
        manage_menu()
    else:
        game =  Game.all.get(user_choice)
        user_input = input(f"Are you sure you would like to delete {game.title}? Enter 'y' or 'n'. ") 
        if user_input == "y":
            game.delete()
            print("Game has been deleted.")
        elif user_input == "n":
            delete_game()
        
    
def view_games_by_id():
    games = Game.get_all()
    games.sort(key=lambda game: game.id)
    print('-------------------------------')
    print("0. Return to previous menu")
    list_games(games)


def view_games_based_on_genre():
    print("Please enter genre:")
    genre_choice = input("> ")
    
    # not sure why Game.all is {} here
    
    found_games = [game for game in Game.get_all() if game.genre.lower() == genre_choice.lower()]
    print(f'Below are the games with genre: "{genre_choice}".')
    print('-------------------------------')
    list_games(found_games)
        

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
    found_games = [game for game in Game.get_all() if game.genre.lower() == genre_choice.lower()]
    for game in found_games:
        print(f'Reviews for {game.title}')
        print('-------------------------------')
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

# def view_reviews_by_id():
#     reviews = Review.get_all()
#     reviews.sort(key=lambda review: review.id)
#     list_reviews(reviews)

def average_rating(reviews):
    ratings = [review.rating for review in reviews]
    total_ratings = sum(ratings)
    average_rating = total_ratings / len(ratings)
    return round(average_rating, 2)

def new_review():
    print("Please select the game you would like to review:")
    view_games_by_id()
    user_choice = int(input("> "))
    if user_choice == 0:
         manage_menu()
    else:
        game = Game.all.get(user_choice)
        print("Please enter the following information:")
        header = input("Enter the header of your review: ")
        rating = int(input("Enter a rating from 1 - 5 (in numbers, or else this crashes): "))
        content = input("Enter the content of your review: ")
        new_review = Review(header, rating, content, game.id)
        new_review.save()
        print("Review successfully added.")
        input("Press enter to display the list of reviews for this game:")
        list_reviews(game.reviews())
    

def update_review():
    found_review = None
    print("Please select the game whose review you would like to update:")
    view_games_by_id()
    game_choice = int(input("> "))
    if game_choice == 0:
        manage_menu()
    else:
        game = Game.all.get(game_choice)
        print('-------------------------------')
        list_reviews(game.reviews())
        while not found_review:
            print("Please enter the header of the review to update or press 0 to return to previous menu:")
            review_choice = input("> ")
            if review_choice == '0':
                break
            else:   
                for review in Review.all.values():
                    if review.header.lower() == review_choice.lower():
                        found_review = review
                        break          
    if not found_review:
        manage_menu()
    else:             
        user_input = input(f"Are you sure you would like to update {review.header}? Enter 'y' or 'n'. ") 
        if user_input == "y":
            review.header = input("Enter the header of your review: ")
            user_rating = None
            while user_rating not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                user_rating = input("Enter a rating from 1 - 10: ")
            review.rating = int(user_rating)         
            review.content = input("Enter the content of your review: ")
            review.update()
            print("Review successfully updated.")
            input("Press enter to display the list of reviews for this game:")
            list_reviews(game.reviews())
        elif user_input == "n":
            update_review()
            
            
def delete_review():
    print("Please select the game you would like to delete a review:")
    print('-------------------------------')
    view_games_by_id()
    game_choice = int(input("> "))
    if game_choice == 0:
        manage_menu()
    else:
        game = Game.all.get(game_choice)
        print('-------------------------------')
        print("0. Return to previous menu")
        list_reviews(game.reviews())
        print("Please enter the header of the review to delete:")
        review_choice = input("> ")
        found_review = None
        for review in Review.all.values():
            if review.header.lower() == review_choice.lower():
                found_review = review
                break
            # check for found_review before proceeding???
        user_input = input(f"Are you sure you would like to delete {review.header}? Enter 'y' or 'n'. ") 
        if user_input == "y":
            review.delete()
            print("Review successfully deleted.")
            input("Press enter to display the list of reviews for this game:")
            list_reviews(game.reviews())
        elif user_input == "n":
            delete_review()