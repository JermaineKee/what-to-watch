import csv

all_movies = {}
all_users = {}


class User:
    def __init__(self, user_id):
        self.id = user_id
        all_users[self.id] = self

class Movie:
    def __init__(self, movie_id, title):
        self.id = movie_id
        self.title = title
        all_movies[self.id] = self
        self.ratings = {} # key: user_id value: Rating object

    def add_rating(self, rating):
        self.ratings[rating.user_id] = rating

    def get_ratings(self):
        return self.ratings.values()


    def __str__(self):
        return 'Movie(movie_id={}, title={})'.format(self.id, repr(self.title))

    def __repr__(self):
        return self.__str__()


class Rating:
    def __init__(self, user_id, movie_id, stars):
        self.user_id = user_id
        self.movie_id = movie_id
        self.stars = stars

        all_movies[self.movie_id].add_rating(self)

    def __str__(self):
        return 'Rating(user_id = {}, movie_id = {}, stars ={})'.format(self.id)


#users =
    # {
    # 1:#######
    # 2:#######
    # 3:#######
    # }








if __name__ == '__main__':
    movie_lib()
