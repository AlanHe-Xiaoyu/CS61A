##################################
# Newton's method (from lecture) #
##################################

def improve(update, close, guess=1, max_updates=100):
    """Iteratively improve guess with update until close(guess) is true."""
    k = 0
    while not close(guess) and k < max_updates:
        guess = update(guess)
        k = k + 1
    return guess

def approx_eq(x, y, tolerance=1e-15):
    """Whether x is within tolerance of y."""
    return abs(x - y) < tolerance

def find_zero(f, df):
    """Return a zero of the function f with derivative df."""
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def newton_update(f, df):
    """Return an update function for f with derivative df."""
    def update(x):
        return x - f(x) / df(x)
    return update

def nth_root_of_a(n, a):
    """Return the nth root of a.

    >>> nth_root_of_a(2, 64)
    8.0
    >>> nth_root_of_a(3, 64)
    4.0
    >>> nth_root_of_a(6, 64)
    2.0
    """
    return find_zero(lambda x: pow(x, n) - a, lambda x: n * pow(x, n-1))

#############
# Questions #
#############

def intersect(f, df, g, dg):
    """Return where f with derivative df intersects g with derivative dg.

    >>> parabola, line = lambda x: x*x - 2, lambda x: x + 10
    >>> dp, dl = lambda x: 2*x, lambda x: 1
    >>> intersect(parabola, dp, line, dl)
    4.0
    """
    "*** YOUR CODE HERE ***"

    def final_func(x):
        return f(x) - g(x)

    def final_deri(x):
        return df(x) - dg(x)

    return find_zero(final_func, final_deri)



from functools import lru_cache
memoize = lru_cache(None)

def six_sided(score):
    if 1 <= score <= 6:
        return 1 / 6
    else:
        return 0


@memoize
def roll_at_least(score, n, dice=six_sided):
    """
    >>> "%.6f" % roll_at_least(1, 1) # rounding to avoid floating point errors
    '1.000000'
    >>> "%.6f" % roll_at_least(2, 2)
    '0.694444'
    >>> "%.6f" % roll_at_least(20, 3)
    '0.000000'
    >>> "%.6f" % roll_at_least(20, 4)
    '0.054012'
    >>> "%.6f" % roll_at_least(20, 9)
    '0.193806'
    >>> "%.6f" % roll_at_least(7, 2)
    '0.527778'
    >>> "%.6f" % roll_at_least(7, 4)
    '0.482253'
    >>> "%.6f" % roll_at_least(14, 4)
    '0.388117'
    >>> "%.6f" % roll_at_least(14, 9)
    '0.193807'
    >>> "%.6f" % roll_at_least(14, 14)
    '0.077887'
    """
    return roll_at_least_ones(score, n, dice) + roll_at_least_no_ones(score, n, dice)

@memoize
def roll_at_least_ones(total, n, dice):
    "*** YOUR CODE HERE ***"
    
    if total > 1:
        return 0

    probability = 1

    for roll in range(n):
        probability *= dice(1)

    return probability


@memoize
def roll_at_least_no_ones(total, n, dice):
    "*** YOUR CODE HERE ***"

    probability = 0

    if n == 1:
        if total <= 1:
            probability = 5 / 6
        elif total > 6:
            probability = 0
        else:
            probability = (6 - total + 1) / 6
    else:
        for current in range(2,7):
            probability += dice(current) * roll_at_least_no_ones(total - current, n - 1, dice)

    return probability

print("Probability of rolling not 1 and 6 is with 1 dice is", roll_at_least(1, 1) - roll_at_least(2, 1) + roll_at_least(6, 1) - roll_at_least(7, 1))
print("Probability of rolling not 1 and 6 is with 2 dice is", roll_at_least(1, 2) - roll_at_least(2, 2) + roll_at_least(6, 2) - roll_at_least(7, 2))
print("Probability of rolling not 1 and 3 is with 3 dice is", roll_at_least(1, 3) - roll_at_least(2, 3) + roll_at_least(6, 3) - roll_at_least(7, 3) + roll_at_least(17, 3) - roll_at_least(18, 3))

print("Probability of rolling exactly score 3/14 with 2 dice is", roll_at_least(3, 2) - roll_at_least(4, 2))
print("Probability of rolling exactly score 3/14 with 3 dice is", roll_at_least(3, 3) - roll_at_least(4, 3) + roll_at_least(14, 3) - roll_at_least(15, 3))
print("Probability of rolling exactly score 3/14/25 with 4 dice is", roll_at_least(3, 4) - roll_at_least(4, 4) + roll_at_least(14, 4) - roll_at_least(15, 4))
print("Probability of rolling exactly score 3/14/25 with 5 dice is", roll_at_least(3, 5) - roll_at_least(4, 5) + roll_at_least(14, 5) - roll_at_least(15, 5) + roll_at_least(25, 5) - roll_at_least(26, 5))

max_prob = 0
max_roll = 0

for score in range(2, 30):
    max_prob = 0
    max_roll = 0
    for roll in range(1, 10):
        if roll_at_least(score, roll) > 0.6:
            max_prob, max_roll = roll_at_least(score, roll), roll
            break
        if roll_at_least(score, roll) > max_prob:
            max_prob, max_roll = roll_at_least(score, roll), roll

    # print(score, "should roll: ", max_roll, "Probability is: ", max_prob)