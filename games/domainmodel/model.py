import datetime


class Publisher:
    def __init__(self, publisher_name: str):
        self.__publisher_name = None
        self.publisher_name = publisher_name  # Use the setter to apply the validation and assignment logic

    @property
    def publisher_name(self) -> str:
        return self.__publisher_name

    @publisher_name.setter
    def publisher_name(self, new_publisher_name: str):
        if not isinstance(new_publisher_name, str) or new_publisher_name.strip() == "":
            self.__publisher_name = None
        else:
            self.__publisher_name = new_publisher_name.strip()  # Always strip whitespace

    def __repr__(self):
        return f"<Publisher {self.publisher_name}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.publisher_name == other.publisher_name

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return False
        # Careful with comparison of NoneTypes, they are not less than or greater than anything
        if self.publisher_name is None or other.publisher_name is None:
            return False
        return self.publisher_name < other.publisher_name

    def __hash__(self):
        return hash(self.publisher_name)


class Genre:
    def __init__(self, genre_name: str):
        self.__genre_name = None
        self.genre_name = genre_name

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    @genre_name.setter
    def genre_name(self, new_genre_name: str):
        if not isinstance(new_genre_name, str) or new_genre_name.strip() == "":
            self.__genre_name = None
        else:
            self.__genre_name = new_genre_name.strip()

    def __repr__(self):
        # we use access via the property here
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__genre_name == other.genre_name

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return False
        # Careful with comparison of NoneTypes, they are not less than or greater than anything
        if self.genre_name is None or other.genre_name is None:
            return False
        return self.genre_name < other.genre_name

    def __hash__(self):
        return hash(self.genre_name)


class Game:
    def __init__(self, game_id, title):
        if isinstance(title, str) and len(title.strip()) != 0:
            self.__title = title.strip()
        else:
            self.__title = None
        if game_id > 0 and isinstance(game_id, int):
            self.__game_id = game_id
        else:
            raise ValueError
        self.__genres = []
        self.__reviews = []

    @property
    def game_id(self) -> int:
        return self.__game_id

    @property
    def genres(self) -> list:
        return self.__genres

    @property
    def reviews(self) -> list:
        return self.__reviews

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        if isinstance(title, str) and len(title.strip()) != 0:
            self.__title = title.strip()
        else:
            self.__title = None

    @property
    def price(self) -> float or int:
        return self.__price

    @price.setter
    def price(self, new_price: float or int):
        if isinstance(new_price, (float, int)) and new_price > 0:
            self.__price = new_price
        else:
            raise ValueError

    @property
    def release_date(self) -> str:
        return self.__release_date

    @release_date.setter
    def release_date(self, new_release_date: str):
        date_format = "%b %d, %Y"
        try:
            datetime.datetime.strptime(new_release_date, date_format)
            self.__release_date = new_release_date
        except ValueError:
            raise ValueError

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, new_description: str):
        if isinstance(new_description, str) and len(new_description.strip()) != 0:
            self.__description = new_description.strip()
        else:
            self.__description = None

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, new_publisher):
        if isinstance(new_publisher, Publisher):
            self.__publisher = new_publisher
        else:
            self.__publisher = None

    @property
    def image_url(self) -> str:
        return self.__image_url

    @image_url.setter
    def image_url(self, new_image_url: str):
        if isinstance(new_image_url, str) and len(new_image_url.strip()) != 0:
            self.__image_url = new_image_url.strip()
        else:
            self.__image_url = None

    @property
    def website_url(self) -> str:
        return self.__website_url

    @website_url.setter
    def website_url(self, new_website_url: str):
        if isinstance(new_website_url, str) and len(new_website_url.strip()) != 0:
            self.__website_url = new_website_url.strip()
        else:
            self.__website_url = None

    def add_genre(self, genre):
        if isinstance(genre, Genre):
            self.__genres.append(genre)

    def remove_genre(self, genre):
        if isinstance(genre, Genre) and genre in self.__genres:
            self.__genres.remove(genre)

    def __repr__(self):
        return f"<Game {self.__game_id}, {self.__title}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__game_id == other.game_id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__game_id < other.game_id

    def __hash__(self):
        return hash(self.__game_id)


class User:
    def __init__(self,username,password):
        if isinstance(password, str) and len(password.strip()) >= 7:
            self.__password = password
        else:
            raise ValueError

        if isinstance(username,str) and len(username.strip())!=0:
            self.__username = username.strip().lower()
        else:
            raise ValueError

        self.__favourite_games = []
        self.__reviews = []

    ### READ ONLY

    @property
    def username(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password

    @property
    def favourite_games(self) -> list:
        return self.__favourite_games

    @property
    def reviews(self)-> list:
        return self.__reviews

    ### READ AND WRITE FUNCTIONS

    def add_favourite_game(self, game):
        if isinstance(game, Game) and game not in self.__favourite_games:
            self.__favourite_games.append(game)

    def remove_favourite_game(self, game):
        if isinstance(game, Game):
            try:
                self.__favourite_games.remove(game)
            except ValueError:
                pass  # game was not in the list

    def add_review(self, review):
        if isinstance(review, Review) and review not in self.__reviews:
            self.__reviews.append(review)

    def remove_review(self, review):
        if isinstance(review, Review):
            try:
                self.__reviews.remove(review)
            except ValueError:
                pass  # review was not in the list
    def __repr__(self):
        return f"<User {self.__username}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__username == other.username

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__username < other.username

    def __hash__(self):
        return hash(self.__username)


class Review:
    def __init__(self,user,game,rating,comment):
        if isinstance(user,User) == 1:
            self.__user = user
        else:
            raise ValueError

        if isinstance(game,Game) == 1:
            self.__game = game
        else:
            raise ValueError

        if (isinstance(rating,int) == 1) and rating in [1,2,3,4,5,6]:
            self.__rating = rating
        else:
            raise ValueError

        if isinstance(comment,str)==1 and len(comment.strip()) != 0:
            self.__comment = comment.strip()

        else:
            raise ValueError


    #READ ONLY
    @property
    def user(self)->User:
        return self.__user
    @property
    def game(self)->Game:
        return self.__game

    ##READ AND WRITE
    @property
    def comment(self)->str:
        return self.__comment

    @comment.setter
    def comment(self, new_comment: str):
        if (isinstance(new_comment,str)==1) and len(new_comment.strip())!=0:
            self.__comment = new_comment.strip()
        else:
            raise ValueError

    @property
    def rating(self)->int:
        return self.__rating

    @rating.setter
    def rating(self, new_rating: int):
        if (isinstance(new_rating,int)==1) and (new_rating in [1,2,3,4,5,6]):
            self.__rating = new_rating
        else:
            raise ValueError

    def __repr__(self):
        return f"Review(User: {self.__user}, Game: {self.__game}, Rating: {self.__rating}, Comment: {self.__comment})"



class Wishlist:
    # TODO
    pass


