from ex_1func import factorial
from ex_1func import butterfly
from ex_1func import vowelcount

def test_factorial():
    assert factorial(9) == 362880‬

def test_butterfly():
    assert butterfly("abyss") == "abyff"

def test_vowelcount():
    assert vowelcount("abyss", 1) == 1
