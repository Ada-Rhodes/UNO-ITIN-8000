"""
This is a module for simulating standard dice rolls
"""
# Import the module random
from random import randint as dieroll


# 4 Sided Die
def d4(n=1):
    total = 0
    for i in range(n):
        total = total + dieroll(1, 4)
    return total


# 6 Sided Die
def d6(n=1):
    total = 0
    for i in range(n):
        total = total + dieroll(1, 6)
    return total


# 8 Sided Die
def d8(n=1):
    total = 0
    for i in range(n):
        total = total + dieroll(1, 8)
    return total


# 10 Sided Die
def d10(n=1):
    total = 0
    for i in range(n):
        total = total + dieroll(1, 10)
    return total


# 12 Sided die
def d12(n=1):
    total = 0
    for i in range(n):
        total = total + dieroll(1, 12)
    return total


# 20 sided die
def d20(n=1):
    total = 0
    for i in range(n):
        total = total + dieroll(1, 20)
    return total


# 100 sided die or D-percentile
def d100(n=1):
    total = 0
    for i in range(n):
        total = total + dieroll(1, 100)
    return total

