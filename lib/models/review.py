from models.__init__ import CONN, CURSOR
from models.game import Game

class Review:
    
    all = {}

    def __init__(self, header, rating, content, game_id, id = None):
        self.id = id
        self.header = header
        self.rating = rating
        self.content = content
        self.game_id = game_id
        
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
        
