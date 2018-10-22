""" Homework 1: Control """

# Q1
from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = lambda a, b: a - b
    # I realized aftewards that the add and sub functions are imported
    # So if lambda is not allowed, this would be: f = sub
    else:
        f = lambda a, b: a + b
    # and this would be: f = add
    return f(a, b)

# Q2
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a ** 2 + b ** 2 + c ** 2 - min(a, b, c) ** 2

# Q3
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"

    assert n > 1
    half = n // 2

    for i in range(half, 1, -1):
        if n % i == 0:
            return i
            
    return 1
            
# Q4
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    2
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    """
    >>> result = with_if_function()
    1
    2
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())

def c():
    return None

def t():
    print(1)
    return

def f():
    print(2)
    return

# Q5
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    number = n
    count = 1
    
    while number != 1:
        print (number)

        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1

        count += 1

    print (number)
    return count

# Q6
quine = "print(repr('print(repr)'))"
"""
"*** YOUR CODE HERE ***"
"""