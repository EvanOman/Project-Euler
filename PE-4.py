"""

Problem 4:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def isPalindrome(n):
    """ Determines if the integer n is a palindrome"""

    # Converts the number into a list of chars
    numList = list(str(n))
    leng = len(numList)

    # Makes sure that all we have are odd length lists to checky
    if not(leng % 2):
        numList.insert(leng/2, 'x')
        leng += 1

    # Now, starting from the center, we compare positions equidistant from the center, if they 
    # are pairwise equivalent, then the number n is a palindrome
    mid = leng // 2
    for i in range(1, leng//2 + 1):
        if not(numList[mid - i] == numList[mid + i]):
            return False
    return True

# First we generate a list of products and their indices (taking commutativity into account)
a = []
for i in range(999,99,-1):
    for j in range(999,i-1,-1):
        a.append((i*j, (i,j)))

# Now we will sort by the products
a.sort(key = lambda tup: tup[0], reverse = True)

# Now we loop over the sorted list and return the first palindrome
for product, (i,j) in a:
    if isPalindrome(product):
        print "%s x %s = %s is the largest palildrome product of 3 digit integers" % (i, j, product)
        break
