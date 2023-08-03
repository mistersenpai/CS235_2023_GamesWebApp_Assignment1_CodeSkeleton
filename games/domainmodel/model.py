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
    def __init__(self,game_id,new_title):
        self.__game_id = None
        self.game_id = game_id

        self.__title = None
        self.title = new_title


    ## READ ONLY FUNCTIONS

    @property
    def game_id(self) -> str:
        return self.__game_id

    @property
    def genres(self) -> str:
        return self.__genres

    @property
    def reviews(self) -> str:
        return self.__reviews

    ## READ AND WRITE FUNCTIONS

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, new_title_name: str):
        if type(new_title_name) == str and len(new_title_name.strip()) != 0:
            self.__title = new_title_name.strip()

    def price(self):
        pass

    def release_date(self):
        pass

    def description(self):
        pass

    def publisher(self):
        pass

    def image_url(self):
        pass

    def website_url(self):
        pass

    def __repr__(self):
        return f"<Game{self.game_id()}, {self.title}>"

    def __eq__(self):
        pass

    def __lt__(self, other):
        pass

    def __hash__(self):
        pass

# class Game:
#     def __init__(self,game_id,new_title):
#         self.__game_id = None
#         self.game_id = game_id
#
#         self.__title = None
#         self.title = new_title
#
#
#     ## READ ONLY FUNCTIONS
#     def game_id(self) -> str:
#         return self.__game_id
#
#     def genres(self):
#         pass
#
#     ## READ AND WRITE FUNCTIONS
#
#     @property
#     def title(self,title) -> str:
#         self.__title = title
#
#     @title.setter
#     def title(self, new_title_name: str):
#         self.__title= new_title_name
#
#     def __repr__(self):
#         return f"<Game {self.game_id}, {self.__title}>"



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