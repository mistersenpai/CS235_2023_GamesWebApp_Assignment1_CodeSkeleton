import pytest
from games.domainmodel.model import Publisher, Genre, Game, Review, User, Wishlist


print('hello world')
class TestArtist:

    def test_construction(self):
        publisher1 = Publisher("Publisher A")
        assert str(publisher1) == "<Publisher Publisher A>"
        publisher2 = Publisher("Publisher B")
        assert str(publisher2) == "<Publisher Publisher B>"
        publisher3 = Publisher("Publisher C")
        assert str(publisher3) == "<Publisher Publisher C>"

        # TODO - the test will fail as the code is incomplete......

    def test_publisher(self):
        # Test 1
        publisher1 = Publisher("Big Fish Games")
        assert str(publisher1) == "<Publisher Big Fish Games>"
        assert publisher1.publisher_name == "Big Fish Games"

        # Test 2
        publisher2 = Publisher("")
        assert publisher2.publisher_name == None

        # Test 3
        publisher3 = Publisher(123)
        assert publisher3.publisher_name == None

        # Test 4
        publisher4 = Publisher(" Wild Rooster   ")
        assert publisher4.publisher_name.strip() == "Wild Rooster"
        publisher4.publisher_name = "Century Game"
        assert str(publisher4) == "<Publisher Century Game>"

# TODO
