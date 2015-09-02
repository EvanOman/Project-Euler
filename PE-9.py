from __future__ import division
import math
"""
Problem 9:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

"""
    For this problem, we are trying to solve for a, b,  and c under the following constraints:

    * a < b < c
    * a, b, c are natural numbers
    * a + b + c = 1000
    * a^2 + b^2 = c^2

    Now making the substitution c = a + b - 1000, we can solve for a in terms of b:

    * a = (2000*b - 1000000) / (2*b - 2000)

    We note that both the numerator and the denominator are positive on the range b < 500

    Then since a must be a natural number, we just need to search for a natrural number
    b < 500 such that 2*b - 2000 divides 2000*b - 1000000. A quick search finds this value
"""

def aVal(b):
    return (2000*b - 1000000) / (2*b - 2000)

b_Sol = -1

# Loop over feasible b values
for b in range(499, 2,-1):

    # If aVal(b) is an integer, then we are done
    a = aVal(b)
    if a.is_integer():
        b_Sol = int(b)
        break
a_Sol = int(aVal(b_Sol))

c_Sol = int(math.sqrt(a_Sol**2 + b_Sol**2))

# Demonstration of valid result:
print "Solutions: a: %s, b: %s, c: %s" % (a_Sol, b_Sol, c_Sol)

print "a + b + c = %s + %s + %s = %s" % (a_Sol, b_Sol, c_Sol, (a_Sol + b_Sol + c_Sol))

print "a^2 + b^2 = c^2 => %s + %s = %s = %s^2" % (a_Sol**2, b_Sol**2, c_Sol**2, c_Sol)

print "a * b * c = %s" % (a_Sol * b_Sol * c_Sol) # Answer is 31875000
