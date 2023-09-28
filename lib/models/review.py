from models.__init__ import CONN, CURSOR
from models.game import Game

class Review:

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Reviews instances """
        sql = """
            CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            header TEXT,
            rating INTEGER,
            content TEXT,
            FOREIGN KEY (game_id) REFERENCES games(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()