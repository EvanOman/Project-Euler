"""

Problem 6:

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

"""
    To solve this problem we will use the following well known identities:

    1. sum_{k = 1}^{n} k    = n(n+1)/2
    2. sum_{k = 1}^{n} k^2  = n(n+1)(2n+1)/6

    Thus we have:

    * Sum of squares:       n(n+1)(2n+1)/6
    * Square of the sum:    (n(n+1)/2)^2
0
"""

def sumOfSq(n):
    return n*(n+1)*(2*n+1)/6

def sqOfSum(n):
    return (n*(n+1)/2)**2

print(abs(sumOfSq(100) - sqOfSum(100)))
