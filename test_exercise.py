from exercise import fattoriale
from exercise import butterfly
from exercise import vowelcount

def test_fattoriale():
    assert fattoriale(3) == 6‬

def test_butterfly():
    assert butterfly("abyss") == "abyff"

def test_vowelcount():
    assert vowelcount("abyss", 1) == 1
