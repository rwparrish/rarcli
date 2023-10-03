The data model must include at least 2 model classes. - Games and Reviews
The data model must include at least 1 one-to-many relationships. - A game has many reviews
Property methods should be defined to add appropriate constraints to each model class. 
Each model class should include ORM methods (create, delete, get all, and find by id at minimum).
Add user inputs/menu structure

STRETCH GOALS:
Once a day for 15 min


9/28 - Next step create/save/drop_table class methods for model classes then go complete faker seeding in seed.py
10/2 - Next step properties, getter/setter and class constraints
10/3 - Update menu in cli.py to reflect below logic and build ORM methods to support menu/DB functionality




MENU:

A user can:
- browse
    - list reviews based on genre
        - enter genre
    - view games based on genre
        - view reviews for a game
    - view games in alpha order
        - view reviews for a game
    - Views games based on average ratings 
        - view reviews for a game

- manage 
    - view games in alpha order (user selects a number) or go up menu
        - enter a new game
        - update a game
        - enter a new review for and existing game (X) 
        - display reviews for chosen game
            - select review and update it
            - select review and delete it       
   

To enter a review, a menu should display all games and their corresponding IDs. The selection is captured from the user input and stored in the review.game_id instance