"""

Promblem 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

import numpy as np
import time


def firstnPrimes1(n):
    primes = np.array([2])
    currInt = 3

    while len(primes) < n :
        if (all(currInt % primes)):
            primes = np.append(primes, currInt)
        currInt += 2
    return primes


def firstnPrimes2(n):
    primes = np.zeros(n)
    primes[0] = 2
    numPrimes = 1
    currInt = 3

    while numPrimes < n :
        isPrime = True
        for p in primes[0:numPrimes]:
            if not(currInt % p):
                isPrime = False
                break

        if isPrime:
            primes[numPrimes] = currInt
            numPrimes += 1


        currInt += 1

    return primes

x = time.time()
a = firstnPrimes1(10001)
print "Time 1: %s" % (time.time() - x)

x = time.time()
a = firstnPrimes2(10001)
print "Time 2: %s" % (time.time() - x)
