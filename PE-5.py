"""
Problem 5:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
import evanUtils as eU

# This problem is asking for the lcm of the first n integers, the following contstructive algorithm
# adds new prime bases as they are found

def lcmTo(n):
    i = 1
    lcm = 1
    while i <= n:
        isPrimePow, base = eU.isPrimePower(i)
        if isPrimePow:
            lcm *= base
        i += 1
    return lcm

# Solves the problem:
print(lcmTo(2))
