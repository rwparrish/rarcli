from models.__init__ import CONN, CURSOR

class Game:
    
    all = {}
    
    def __init__(self, title, year, genre, multiplayer, description, id = None):
        self.id = id
        self.title = title
        self.year = year
        self.genre = genre
        self.multiplayer = multiplayer
        self.description = description
        
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
        
        
    