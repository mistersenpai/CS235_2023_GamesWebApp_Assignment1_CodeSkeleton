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
        self.__review= []



    '''
    READ ONLY FUNCTIONS
    '''
    @property
    def game_id(self) -> int:
        return self.__game_id

    @property
    def genres(self) -> list:
        return self.__genres

    @property
    def reviews(self) -> list:
        return self.__reviews

    '''
    READ AND WRITE FUNCTIONS
    '''

    @property
    def title(self) ->str:
        return self.__title

    @title.setter
    def title(self, title:str):
        if isinstance(title, str) == True and len(title.strip()) != 0:
            self.__title = title.strip()
        else:
            self.__title = None

    @property
    def price(self) -> int or float:
        return self.__price

    @price.setter
    def price(self, new_price: int or float):
        if (isinstance(new_price, str)== True or isinstance(new_price, float)== True) and new_price > 0:
            self.__price = new_price
        else:
            raise ValueError


    @property
    def release_date(self) -> str:
        return self.__release_date

    @release_date.setter
    def release_date(self, new_date: str):
        formatted = "%b %d, %Y"
        try:
            datetime.datetime.strptime(new_date, formatted)
            self.__release_date = new_date
        except ValueError:
            raise ValueError

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, new_desc):
        if (isinstance(new_desc, str) == True) and len(new_desc.strip()) != 0:
            self.__description = new_desc.strip()
        else:
            self.__description = None

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, new_pub):
        if isinstance(new_pub, Publisher) == True:
            self.__publisher = new_pub
        else

    @property
    def image_url(self) -> str:
        pass

    @property
    def website_url(self) -> str:
        pass




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