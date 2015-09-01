"""

Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

import math

import evanUtils as eU

# My technique is pretty simple: starting at the sqrt of n, simply iterate downwards
# and return the first number which both divides n and is prime
def largestPrimeFactor(n):
    if eU.isPrime(n):
        return 1

    for i in range(int(math.sqrt(n)), 1, -1):
        if (n % i == 0):
            if eU.isPrime(i):
                return i

    print("ERROR")
    return -1

# SOLVES THE PROBLEM:
print(largestPrimeFactor(600851475143))
