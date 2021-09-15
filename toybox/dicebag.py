"""
This is a module for simulating standard dice rolls
"""
# Import the module random
from random import randint as dieroll


# 4 Sided Die
def d4():
    return dieroll(1, 4)


# 6 Sided Die
def d6():
    return dieroll(1, 6)


# 8 Sided Die
def d8():
    return dieroll(1, 8)


# 10 Sided Die
def d10():
    return dieroll(1, 10)


# 12 Sided die
def d12():
    return dieroll(1, 12)


# 20 sided die
def d20():
    return dieroll(1, 20)


# 100 sided die or D-percentile
def d100():
    return dieroll(1, 100)

