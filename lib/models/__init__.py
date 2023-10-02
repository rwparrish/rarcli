import sqlite3

CONN = sqlite3.connect('game_reviews.db')
CURSOR = CONN.cursor()
