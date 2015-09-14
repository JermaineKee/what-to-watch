import csv

all_movies = {}
all_users = {}

def users():
    with open('ml-100k/u.user') as f:
        reader = csv.DictReader(f, category = ['user_id'], delimeter = '|')
        for row in reader:
            User(int(row['user_id']))
def movies():
    with open('ml-100k/u.item', encoding = 'latin_1') as f:
        reader = csv.DictReader(f, category = ['movie_id', 'movie_title', '', '', 'something_else' ],  delimeter = '|',)
        for row in reader:
            Movie(int(row['movie_id']), row['movie_title'])

def ratings():
    with open('ml_100k/u.data') as f:
        reader = csv.DictReader(f, category = ['user_id', 'item_id', 'rating'], delimeter = '|' )
        for row in reader:
            Rating(int(row['user_id']), int(row['item_id']), int(row['rating']))


class User:
    "setting up 'User' class"
    def __init__(self, user_id, rating):
        self.id = user_id
        self.rating = {}
        all_users[self.id] = self


    def add_user_rating(self, rating):
        self.ratings[rating.item_id] = rating

    def get_ratings(self):
        return sorted(self.ratings.values(), reverse=True)

    def get_top_rated(self,num):
        return sorted([x for x in all_movies.values()
                        if x.id not in self.ratings],
                    key = lambda m: m.avg_ratings(), reverse = True) [:num]

class Movie:
    "setting up 'Movie' class"
    def __init__(self, movie_id, title):
        self.id = movie_id
        self.title = title
        all_movies[self.id] = self
        self.ratings = {} # key: user_id value: Rating object

    def add_rating(self, rating):
        self.ratings[rating.user_id] = rating

    def get_ratings(self):
        return sorted(self.ratings.values(), reverse=True)

    def ave_ratings(self):
        return sum(get_ratings(self))/len(get_ratings(self))


    def __str__(self):
        return 'Movie(movie_id={}, title={})'.format(self.id, repr(self.title))

    def __repr__(self):
        return self.__str__()


class Rating:
    "setting up 'Rating' class"
    def __init__(self, user_id, movie_id, stars):
        self.user_id = user_id
        self.movie_id = movie_id
        self.stars = stars

        all_movies[self.movie_id].add_rating(self)
        all_users[self.user_id].add_user_rating(self)


    def __str__(self):
        return 'Rating(user_id = {}, movie_id = {}, stars ={})'.format(self.id)


def euclidean_distance(v, w):
    """Given two lists, give the Euclidean distance between them on a scale
    of 0 to 1. 1 means the two lists are identical.
    """

    # Guard against empty lists.
    if len(v) is 0:
        return 0

    # Note that this is the same as vector subtraction.
    differences = [v[idx] - w[idx] for idx in range(len(v))]
    squares = [diff ** 2 for diff in differences]
    sum_of_squares = sum(squares)

    return 1 / (1 + math.sqrt(sum_of_squares))



#users =
    # {
    # 1:#######
    # 2:#######
    # 3:#######
    # }








if __name__ == '__main__':
    movie_lib()
