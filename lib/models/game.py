from models.__init__ import CONN, CURSOR
import ipdb


class Game:
    
    all = {}
    
    def __init__(self, title, year, genre, multiplayer, description, id = None):
        self.id = id
        self.title = title
        self.year = year
        self.genre = genre
        self.multiplayer = multiplayer
        self.description = description
        
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        self.__title = title
        
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, year):
        if not isinstance(year, str):
            raise TypeError("Year must be a string")
        self.__year = year
        
    @property
    def genre(self):
        return self.__genre
    
    @genre.setter
    def genre(self, genre):
        if not isinstance(genre, str):
            raise TypeError("Genre must be a string")
        self.__genre = genre
        
    @property
    def multiplayer(self):
        return self.__multiplayer
    
    @multiplayer.setter
    def multiplayer(self, multiplayer):
        if multiplayer in [0, 1]:
            self.__multiplayer = multiplayer
        else:
            raise TypeError("Multiplayer entry is not a zero or one")
        
    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, description):
        if not isinstance(description, str) or not len(description) >= 10:
            raise TypeError("Description must be a string and at least 10 characters")
        self.__description = description
        
        
        
    def save(self):
        """ Persist the attributes of a Game instance to the database """
        sql = """
            INSERT INTO games (title, year, genre, multiplayer, description)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.year, self.genre, self.multiplayer, self.description))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Games instances """
        sql = """
            CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY,
            title TEXT,
            year TEXT,
            genre TEXT,
            multiplayer INTEGER,
            description TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        """ Drop the table if it exists """
        sql = """
            DROP TABLE IF EXISTS games
        """
        CURSOR.execute(sql)
        CONN.commit()
        
        
    @classmethod
    def instance_from_db(cls, row):
        
        """Return a Game object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        game = cls.all.get(row[0])
        if game:
            # ensure attributes match row values in case local instance was modified
            game.title = row[1]
            game.year = row[2]
            game.genre = row[3]
            game.multiplayer = row[4]
            game.description = row[5]

        else:
            # not in dictionary, create new instance and add to dictionary
            game = cls(row[1], row[2], row[3], row[4], row[5])
            game.id = row[0]
            cls.all[game.id] = game
        return game
    
    @classmethod
    def find_by_id(cls, id):
        """Return a game object with a matching id"""
        sql = """
            SELECT *
            FROM games
            WHERE id is ?
        """
        
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row)
    
    
    @classmethod
    def get_all(cls):
        """Return a list containing a Game object per row in the table"""
        sql = """
            SELECT *
            FROM games
        """
        
        rows = CURSOR.execute(sql).fetchall()
        # game dict for row in rows
        return [cls.instance_from_db(row) for row in rows]
        
    @classmethod   
    def find_games_by_genre(cls, genre):
        """Return a game objects corresponding to the table rows with the matching genre"""
        sql = """
            SELECT *
            FROM games
            WHERE genre is ?
        """

        rows = CURSOR.execute(sql, (genre,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    # def get_review_ratings(self, identifier):
    #     """Get list of ratings for reviews of this game looked up by title or id"""
    #     if isinstance(identifier, int):
    #     # Look up by id
    #     game = Game.find_by_id(identifier) 
    #     else:
    #     # Look up by title 
    #     game = next((g for g in Game.get_all() if g.title == identifier), None)

    #     if not game:
    #     raise ValueError("No game found")
        
    #     ratings = []
    #     for review in Review.find_by_game(game.id):
    #     ratings.append(review.rating)

    #     return ratings