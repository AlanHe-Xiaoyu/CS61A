from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

dice = six_sided
total = 0
iterations = 10000
ones = 0

for i in range(iterations):
    a = dice()
    b = dice()
    c = dice()
    d = dice()
    e = dice()
    f = dice()
    g = dice()

    if (a == 1) or (b == 1):
        total += 1
    else:
        total += a + b 

print ("Expected value for two: ", format(total / iterations, '.5f'))