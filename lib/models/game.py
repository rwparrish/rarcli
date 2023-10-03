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
        
        
    