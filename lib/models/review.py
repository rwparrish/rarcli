from models.__init__ import CONN, CURSOR
from models.game import Game
import ipdb

class Review:
    
    all = {}

    def __init__(self, header, rating, content, game_id, id = None):
        self.id = id
        self.header = header
        self.rating = rating
        self.content = content
        self.game_id = game_id
        
    @property
    def header(self):
        return self.__header
    
    @header.setter
    def header(self, header):
        if not isinstance(header, str):
            raise TypeError("Header must be a string")
        self.__header = header
        
    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self, rating):
        if not isinstance(rating, int):
            raise TypeError("Rating must be an integer")
        if rating < 1 or rating > 10:
            raise ValueError("Rating must be between 1 and 10")
        self.__rating = rating
    
    @property
    def content(self):
        return self.__content
    
    @content.setter
    def content(self, content):
        if not isinstance(content, str) or not len(content) >= 10:
            raise TypeError("Content must be a string and at least 10 characters")
        self.__content = content
        
    @property
    def game_id(self):
        return self.__game_id
    
    @game_id.setter
    def game_id(self, game_id):
        if not isinstance(game_id, int):
            raise TypeError("Game ID must be an integer")
        game = Game.find_by_id(game_id)
        if not game:
            raise ValueError("Game ID does not exist")
        self.__game_id = game_id
    
        
    def save(self):
        """ Persist the attributes of a Review instance to the database """
        sql = """
            INSERT INTO reviews (header, rating, content, game_id)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.header, self.rating, self.content, self.game_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Reviews instances """
        sql = """
            CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            header TEXT,
            rating INTEGER,
            content TEXT,
            game_id INTEGER,
            FOREIGN KEY (game_id) REFERENCES games(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        """ Drop the table if it exists """
        sql = """
            DROP TABLE IF EXISTS reviews
        """
        CURSOR.execute(sql)
        CONN.commit()
        
        
    @classmethod
    def instance_from_db(cls, row):
        """Return a Game object having the attribute values from the table row."""
        # Check the dictionary for an existing instance using the row's primary key
        review = cls.all.get(row[0])
        if review:
            # ensure attributes match row values in case local instance was modified
            review.header = row[1]
            review.rating = row[2]
            review.content = row[3]
            review.game_id = row[4]
            
        else:
            # not in dictionary, create new instance and add to dictionary
            review = cls(row[1], row[2], row[3], row[4])
            review.id = row[0]
            cls.all[review.id] = review
        return review
        
    @classmethod
    def reviews_by_game_id(cls, game_id):
        """ Return all reviews for a given game """
        sql = """
            SELECT * FROM reviews WHERE game_id = ?
        """
        CURSOR.execute(sql, (game_id,))
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]
       

