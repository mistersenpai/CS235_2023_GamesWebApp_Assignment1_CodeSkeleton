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
    def __init__(self,game_id,title):

        if isinstance(title, str) and len(title.strip()) < 1:
            self.__title = title.strip()
        else:
            self.__title = None

        if game_id > 0 and type(game_id) == int:
            self.__game_id = game_id
        else:
            raise ValueError


        self.__genres = []
        self.__review=[]




class User:
    # TODO
    pass


class Review:
    # TODO
    pass


class Wishlist:
    # TODO
    pass


game1 = Game(1, "Super Soccer Blast")
print(game1)

game3 = Game(2, "Super Soccer Blast")
print(game3)