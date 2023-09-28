from models.__init__ import CONN, CURSOR

class Game:

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
            description TEXT,)
        """
        CURSOR.execute(sql)
        CONN.commit()