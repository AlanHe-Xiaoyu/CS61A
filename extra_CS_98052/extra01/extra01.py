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

def find_zero(f, df, guess=1):
    """Return a zero of the function f with derivative df."""
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero, guess)

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

def differentiate(f, delta=1e-5):
    """Approximately differentiate a single-argument function.

    >>> differentiate(lambda x: x*x)(4)  # should be close to 8
    7.999999999785955
    """
    return lambda x: (f(x + delta) - f(x - delta)) / (2 * delta)

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
    

def print_updates(f, df, x, k, digits=4):
    """Print the first k Newton guesses for a zero of f, starting at x.

    >>> print_updates(lambda x: x*x - 2, lambda x: 2*x, 1, 4)
    1, 1.5, 1.4167, 1.4142, 1.4142
    """
    update = newton_update(f, df)
    guesses = [x]
    for _ in range(k):
        guesses.append(update(guesses[-1]))
    print(*[round(guess, digits) for guess in guesses], sep=', ')

def cycle(f, df, k, guess):
    """Find a k-step cycle in Newton's method starting near guess.

    >>> f = lambda x: x*x*x - 8*x*x + 17*x - 3
    >>> df = lambda x: 3*x*x - 16*x + 17
    >>> f(find_zero(f, df, 1)) # Starting at a guess of 1 finds a zero
    0.0
    >>> print_cycle = lambda k, x: print_updates(f, df, cycle(f, df, k, x), k)
    >>> print_cycle(3, 4.2)  # A 3-step cycle starting near 4.2
    4.2123, 3.7175, 4.7112, 4.2123
    >>> print_cycle(3, 3.7)  # A 3-step cycle starting near 3.7 (the same cycle)
    3.7175, 4.7112, 4.2123, 3.7175
    >>> print_cycle(5, 4)    # A 5-step cycle starting near 4
    4.003, 3.0234, 3.7591, 5.0564, 4.4548, 4.003
    """
    "*** YOUR CODE HERE ***"

    left = guess
    right = guess
    update = newton_update(f, df)
    count_cycle = 0

    while count_cycle < 10000:
        init_left = left
        # init_right = right

        for i in range(k):
            left = update(left)
            # right = update(right)

        if approx_eq(left, init_left, 1e-7):
            return init_left
        else:
            # left = init_left + differentiate(lambda x: x * x / 4, delta=1e-5)(init_left - left)
            left = init_left + (init_left - left) * 1e-3
            count_cycle += 1

"""
f = lambda x: x*x*x - 8*x*x + 17*x - 3
df = lambda x: 3*x*x - 16*x + 17
a = 3.7175
for i in range(3):
    a = newton_update(f, df)(a)
    print(a)
    print(approx_eq(a, 4.2123, 1e-5))
"""