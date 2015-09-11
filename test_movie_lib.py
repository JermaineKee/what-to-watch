from movie_lib import *

def tes_user_creation():
    user1 = User(5)
    user2 = User(12)
    assert user1.id == 5
    assert user2.id == 12


def tes_movie_creation():
    movie1 = Movie(3, 'Toy Story')
    movie2 = Movie(9, 'Pretty Woman')
    assert movie1.id == 3
    assert movie1.title == 'Toy Story'
    assert movie2.id == 9
    assert movie2.title == 'Pretty Woman'
