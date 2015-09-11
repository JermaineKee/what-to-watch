from movie_lib import *

ebert = user(5)
siskel = user(12)
movie1 = Movie(3, 'Toy Story')
movie2 = Movie(9, 'Pretty Woman')

rating1 = Rating(siskel.id, movie1.id, 4)
rating2 = Rating(ebert.id, movie2.id, 1)
rating3 = Rating(siskel.id, movie2.id, 3)
rating4 = Rating(ebert.id, movie1.id, 1)

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

def test_rating_creation():
    assert rating1.user_id == rating3.user_id == siskel.id
    assert rating2.user_id == rating4.user_id == ebert.id
    assert ratings1.movie_id == rating4.movie_id == movie1.id
    assert ratings2.movie_id == rating3.movie_id == movie2.id


def test_find_ratings_for_movie():
    # toy_story_ratings = get_ratings_for_movie(movie1.id)
    # or
    # returns a list of all ratings for that movie
    toy_story_ratings = all_movies[movie1.id].get_ratings()
