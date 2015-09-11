import csv


class User:
    def __init__(self, user_id):
        self.id = user_id

class Movie:
    def __init__(self, movie_id, title):
        self.id = movie_id
        self.title = title


class Rating:
    def __init__(self, user_id, movie_id, stars):
        self.user_id = user_id
        self.movie_id = movie_id
        self.stars = stars

    def __str__(self):
        return User(id = {}).format(self.id)


#users =
    # {
    # 1:#######
    # 2:#######
    # 3:#######
    # }








if __name__ == '__main__':
    movie_lib()
