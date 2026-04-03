import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word,expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
    ("abcdefghijklmnopqrstuvwxyz", True),
    ("Aa", False),
    ("aA", False),
    ("abcdeFghIjklmnOpqrStuvWxYz", True),
])
def test_is_isogram(word, expected):
    assert is_isogram(word) == expected

def test_single_letter():
    assert is_isogram("a") == True
    assert is_isogram("Z") == True

def test_repeated_letters_in_long_word():
    assert is_isogram("subdermatoglyphic") == True
    assert is_isogram("alphabet") == False
