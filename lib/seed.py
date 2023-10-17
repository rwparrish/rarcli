# from models.__init__ import CONN, CURSOR
from models.game import Game
from models.review import Review
from faker import Faker
from faker.providers import BaseProvider

# create custom provider for video game genres
class VideoGameGenreProvider(BaseProvider):
    def video_game_genre(self):
        genres = ["Action", "Adventure", "RPG", "Simulation", "Strategy", "Sports", "Puzzle", "Horror", "Platformer"]
        return self.random_element(genres)
    
fake = Faker()
fake.add_provider(VideoGameGenreProvider)


def seed_database():
    
    Game.drop_table()
    Review.drop_table()
    Game.create_table()
    Review.create_table()
    
    for i in range(50):
        game = Game(title=fake.sentence(nb_words=3)[:-1], year=fake.year(), genre=fake.video_game_genre(), multiplayer=fake.boolean(), description=fake.text())
        game.save()
        for i in range(5):
            review = Review(header=fake.word(), rating=fake.random_int(min=1, max=10), content=fake.text(), game_id=game.id)
            review.save()
            
    
seed_database()
print("Seeded database")
    