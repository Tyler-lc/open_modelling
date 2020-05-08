from func import factorial
from func import butterfly
from func import vowelcount

def test_factorial():
    assert factorial(3) == 6‬

def test_butterfly():
    assert butterfly("abyss") == "abyff"

def test_vowelcount():
    assert vowelcount("abyss", 1) == 1
