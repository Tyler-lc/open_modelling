def fattoriale(x):
    """
    this function returns the factorial of a number x
    to store the value in a variable use value = factorial(x)
    """
    f = 1
    if x == 0:
        return f

    else:
        for i in range(x):
            f = f * (i + 1)
        return f


def butterfly(s):
    """ converts a string into butterfly language. Every S is converted into an F.
    For example: butterfly("abyss") returns abyff

    Args:
        s(str) = the string that needs to be converted in butterfly language

    Returns:
        str -> a string where all S have been changed in to F

    """
    l1 = []
    if isinstance(s, str) == False:
        return "inserted value is not a string"

    else:
        for i in s:
            if i == "s":
                l1.append("f")
            else:
                l1.append(i)
    return "".join(l1)


def vowelcount(s, y):
    """
    this function counts the amounts of vowels in a string
    insert y = 1 counts the letter y as a vowel
    if y = 0 the letter y is not counted as vowel

    Args:
        s = type(str). It's the string you want to count for vowels
        y = type(int). If y == 1 the letter Y is counted as vowel, otherwise it is not.
    Returns:
        int number of vowels in the word or sentence
    """
    n = 0
    vowels = ["a", "e", "i", "o", "u"]
    vowels_y = ["a", "e", "i", "o", "u", "y"]

    if isinstance(s, str) == False:
        return "inserted value is not a string"

    if y != 1 and y != 0:
        return "wrong y value. y must be either 1 or 0"

    else:
        if y == 1:
            for i in s:
                if i in vowels_y:
                    n = n+1
                else:
                    pass
        if y == 0:
            for i in s:
                if i in vowels:
                    n = n+1
                else:
                    pass
    return n

    # add some comments to check some stuff on the repository
