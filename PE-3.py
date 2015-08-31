"""

Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

import math

# My technique is pretty simple: starting at the sqrt of n, simply iterate downwards
# and return the first number which both divides n and is prime
def largestPrimeFactor(n):
    if isPrime(n):
        return 1

    for i in range(int(math.sqrt(n)), 1, -1):
        if (n % i == 0):
            if isPrime(i):
                return i

    print("ERROR")
    return -1

# The miller rabin primality test for n < 341550071728321
# as described here: http://primes.utm.edu/prove/prove2_3.html , the most important part is:
# Write n-1 = (2^s)d where d is odd and s is non-negative: n is a strong probable-prime base a (an a-SPRP) if either a^d = 1 (mod n) or (a^d)^(2r) = -1 (mod n) for some non-negative r less than s.
def isPrime(n):
    if n > 341550071728321:
        print("Error: Number too large")
        return False

    primeList = getPrimeList(n)

    # Initializing the d and s parameters
    d,s = n-1,0
    while not(d%2):
        d,s = d >>1, s+1

    return not(any(tryComposite(a, d, n, s) for a in primeList))

def tryComposite(a,d,n,s):
    if pow(a,d,n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d,n) == n - 1:
            return False
    return True


def getPrimeList(n):
    demarcNums = [1373653, 25326001, 118670087467,2152302898747,341550071728321]

    if n > demarcNums[-1]:
        print("Number is too large!!")
        return -1
    for i, num in enumerate(demarcNums):
        if (n < num):
            case = i
            break

    lists = {0: (2,3),
             1: (2,3,5),
             2: (2,3,5,7),
             3: (2,3,5,7,11),
             4: (2,3,5,7,11,13,17)
             }
    return lists[case]


# SOLVES THE PROBLEM:
print(largestPrimeFactor(600851475143))
