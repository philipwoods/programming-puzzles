# File: projecteuler.py
# Contains the functions that I used to solve each problem in Project Euler.

# Problems solved:   1   2   3   4   5   6   7   8   9  10
#                   11  12  13  14  15  16  17  18  19  20
#                   21  22      24  25
#                               34
#                                               48
#                   
#                                           67

import math
import array
import datetime

filepath_base = "C:\Users\Philip\Dropbox\git_projects\programming-puzzles\project-euler\\"

# PROBLEM 1

def multiples35( maxi ):
    """
    Finds the sum of all of the multiples of 3 or 5 less than the input.
    """
    SUM = 0
    for i in range(1,maxi):
        if not i % 3 or not i % 5:
            SUM += i
    return SUM

# PROBLEM 2

def evenFib( maxi ):
    """
    Finds the sum of the even Fibonacci numbers less than the input.
    """
    SUM = 0
    num1 = 1
    num2 = 1
    while num2 <= maxi:
        if not num2 % 2:
            SUM += num2
        num2 = num2 + num1
        num1 = num2 - num1
    return SUM

# PROBLEM 3

def largestPrimeFactor( inp ):
    """
    Finds the largest prime factor of the input.
    """
    factors = primeFactors2(inp)
    if bool(factors):
        return max(factors)

def primeFactors( inp ):
    """
    Finds the prime factors of the input.
    """
    potential = sieve(inp/2+1)
    factors = []
    for i in potential:
        if not inp % i:
            factors.append(i)
    if factors == []:
        print "That number is prime."
    else:
        return factors

def primeFactors2( inp ):
    """
    A less memory-limited and faster version of primeFactors that also gives
    the multiplicity of each factor.
    """
    factors = []
    # Remove all of the factors of 2
    while not inp % 2:
        factors.append(2)
        inp /= 2
    # Perform the same process on all odd factors.
    # This will involve checking some composite numbers, but their factors will
    # have been removed already (factors must be smaller than the composite) so
    # the check inp % i will never succeed for them.
    i = 3
    while i**2 <= inp:
        while not inp % i:
            factors.append(i)
            inp /= i
        i += 2
    # At this point, anything left must also be prime. Any factor larger than
    # inp**0.5 must have its complementary factor smaller than that, so since
    # we remove every factor we find, we will have found all of the factors
    # by the time we iterate up to the square root.
    if inp > 1:
        factors.append(inp)
    return factors

def sieve( inp ):
    """
    Performs the sieve of Erastothenes to find all primes below the input.
    """
    if inp < 3:
        return []
    result = range(3,inp,2)
    result.insert(0,2)
    for i in range(3,int(inp**0.5)+1):
        start = i**2
        for j in range(inp):
            toRemove = start + j * i
            if toRemove > inp or toRemove not in result:
                continue
            result.remove(start + j * i)
    return result

# PROBLEM 4

def isPalindrome( inp ):
    """
    Determines whether a given input is a palindrome when converted to a string.
    """
    string = str(inp)
    length = len(string)
    i = 0
    while i < length/2:
        if string[i] != string[length-i-1]:
            return False
        i += 1
    return True

def findLargePal():
    biggest = 0
    for i in range(100,1000):
        for j in range(100,i+1):
            potential = i * j
            if isPalindrome(potential) and potential > biggest:
                biggest = potential
    return biggest

# PROBLEM 5

"""
For this, we need a number that contains the least possible prime factors
while still including at least as many as each individual number.

1, 2, 3, 4=2*2, 5, 6=2*3, 7, 8=2*2*2, 9=3*3, 10=2*5, 11, 12=2*2*3, 13,
14=2*7, 15=3*5, 16=2*2*2*2, 17, 18=2*3*3, 19, 20=2*2*5
 
Therefore we need 1 * 2*2*2*2 * 3*3 * 5 * 7 * 11 * 13 * 17 * 19 = 232792560
"""

# PROBLEM 6

def sumOfSquares( inp ):
    """
    Returns the sum of the squares of the numbers up to the input.
    """
    return inp*(inp+1)*(2*inp+1)/6

def squareOfSum( inp ):
    """
    Returns the square of the sum of the numbers up to the input.
    """
    sums = (1+inp)*inp/2
    return sums**2

def difference( inp ):
    """
    Returns the difference between the square of the sum and the sum of the
    squares of the numbers up to the input.
    """
    return abs( squareOfSum(inp) - sumOfSquares(inp) )

# PROBLEM 7

def sieve2( inp ):
    """
    Performs the sieve of Erastothenes to find all primes between 50000 and
    the input. Assumes input larger than 50000.
    """
    result = range(49999,inp,2)
    for i in range(3,int(inp**0.5)+1):
        start = i**2
        for j in range(inp):
            toRemove = start + j * i
            if toRemove > inp or toRemove not in result:
                continue
            result.remove(start + j * i)
    return result

def find10001stPrime( inp ):
    """
    Putting what I did in shell into a function.
    """
    a = sieve(50000)
    b = sieve2(105000)
    b.remove(49999)
    a.extend(b)
    assert len(a) > 10001
    return a[10000]

# PROBLEM 8

def listProduct( L ):
    """
    Takes a list of integers and returns the product of all of the integers.
    """
    i = 0
    product = 1
    while i < len(L):
        product *= L[i]
        i += 1
    return product

def greatestProduct( inp ):
    """
    Returns the largest product of five consecutive digits in the input integer.
    """
    biggest = 0
    l = list(str(inp))
    l = map(int,l)
    i = 5
    while i <= len(l):
        candidate = listProduct(l[i-5:i])
        if candidate > biggest:
            biggest = candidate
        i += 1
    return biggest

# PROBLEM 9

"""
I found that a formula for generating Pythagorean triples (a, b, c such that
a**2 + b**2 = c**2) holds that for integers m and n with m > n:

a = m**2 - n**2
b = 2 * m * n
c = m**2 + n**2

We know a + b + c = 1000, so therefore 500 = m*(m+n) and n = 500/m - m
which implies that m is a divisor of 500.  This results in the possible values
of m and n shown below:

  m  |  n
-----------
   1 | 499
   2 |  *
   4 |  *
   5 |  *
  10 |  40
  20 |   5

The (m,n) = (20,5) is the only pair that also satisfies the m > n requirement.
This means that a = 375, b = 200, and c = 425. These are in fact a Pythagorean
triple, and they add up to 1000. We see that the product is a*b*c = 31875000.
"""

# PROBLEM 10

def isPrime( inp ):
    """
    Checks if the input is a prime number or not.
    """
    if not inp % 2:
        return False
    i = 3
    while i**2 <= inp:
        if not inp % i:
            return False
        i += 2
    return True

def sumPrimes( inp ):
    """
    Determines the sum of all primes less than the input.
    """
    total = 0
    if inp >= 2:
        total += 2
    i = 3
    while i < inp:
        if isPrime(i):
            total = total + i
        i += 1
    return total

# PROBLEM 16

def digitSum(num):
    """
    Converts input number to list of digits, then sums the list.
    """
    digits = [int(i) for i in str(num)]
    def sumSeq(seq):
        def add(x,y): return x + y
        return reduce(add, seq, 0)
    return sumSeq(digits)

# PROBLEM 20

def factorial(num):
    """
    Returns the factorial of the input number.
    """
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
# digitSum(factorial(100))

# PROBLEM 14

def collatz(num, lengths={}):
    """
    Returns the length of the sequence required to reach 1 from the input
    using the Collatz rule.
    """
    if num in lengths:
        return lengths[num]
    if num == 1:
        lengths[num] = 1
    elif num % 2 == 0:
        lengths[num] = 1 + collatz(num/2,lengths)
    else:
        lengths[num] = 2 + collatz((3*num+1)/2,lengths)
    return lengths[num]

def collatzLongSeq(maxValue):
    """
    Finds the longest Collatz sequence for positive integers less than the input
    and returns the starting number and the length for that sequence.
    """
    lengths = {} # Stores collatz inputs as keys, sequence lengths as values
    results = {} # Stores sequence lengths as keys, starting number as values
    for i in range(1,maxValue):
        results[collatz(i,lengths)] = i
    maximum = max(results.keys()) # Gets the largest path length
    return (results[maximum],maximum)

# PROBLEM 13

def sumDigits(numDigits):
    """
    Returns the first numDigits digits of the sum of the numbers found in the
    file p13.txt.
    """
    f = open(filepath_base + "p13.txt")
    numbers = f.readlines()
    sigDigits = []
    for number in numbers:
        sigDigits.append(int(number[0:numDigits+2])) #**#
    result = sum(sigDigits)
    return int(str(result)[0:numDigits])

# There is a very small chance that this method will give and incorrect answer
# given an arbitrary set of numbers, maybe 0.5%? The precision can be increased
# by increasing the extra digits included in the marked line.

# PROBLEM 25

def longFib(numDigits):
    """
    Returns which Fibonacci term is the first to have numDigits digits.
    """
    limit = 10**(numDigits-1)
    numbers = {}
    i = 1
    while fibonacci(i,numbers) < limit:
        i += 1
    return i

def fibonacci(n, numbers={}):
    """
    Returns the nth Fibonacci number.
    """
    if n in numbers:
        return numbers[n]
    if n == 1 or n == 2:
        numbers[n] = 1
    else:
        numbers[n] = fibonacci(n - 1, numbers) + fibonacci(n - 2, numbers)
    return numbers[n]

# PROBLEM 12

def divisor(n,x):
    """
    Returns sigma_x(n).
    """
    if n == 1:
        return 1
    pf1 = primeFactors2(n) # Get a list of the prime factors of n
    pf2 = []
    # Reformat list from [1, 2, 2, 2, 3, 3, 5] to [(1,1),(2,3),(3,2),(5,1)]
    # Assumes pf1 is sorted.
    for p in pf1:
        count = pf1.count(p)
        pf2.append((p,count))
        del pf1[0:count - 1]
        
    # sigma_x(n) = Prod( Sum( p_i^(j*x), j=0, a_i ), i=1, r )
    # r = number of distinct prime factors of n
    # p_i = ith prime factor
    # a_i = max power of p_i by which n is divisible
    totalProd = 1
    for i in range(len(pf2)):
        powerSum = 0
        for j in range(pf2[i][1]+1):
            powerSum += pf2[i][0]**(j*x)
        totalProd *= powerSum
    return totalProd

def triangleNum(n):
    """
    Returns the nth triangle number.
    """
    return n*(n+1)/2

def triangleDiv(numDiv):
    """
    Returns the first triangle number with more than numDiv divisors.
    """
    i = 1
    while divisor(triangleNum(i),0) <= 500:
        i += 1
    return triangleNum(i)

# PROBLEM 15

def cbc(n):
    """
    Returns the nth central binomial coefficient.
    """
    return factorial(2*n)/factorial(n)**2

# I'm not completely sure what the formulaic basis for this is, but it seems
# that the nth central binomial coefficient is the number of paths through
# an n by n grid when only moving right or down.
# Another interesting way to think about it is like memoizing in a way.  This
# results in the hypothesis that for an n by n grid, the number of paths
# through it is P(n,n) = 2 * ( 2 * P(n-1,n-1) - P(n-1,n-2) + P(n,n-3) ).
# See p15.xlsx for an explanation better than this.
# I noticed the cbc thing while pursuing the second method.

# PROBLEM 17

def countLetters(number):
    """
    Returns the number of letters in the written form of the input.
    Assumes the number is not greater than 1000.
    """
    # Set the number of letters in each digit
    digits = [0,3,3,5,4,4,3,5,5,4]
    teens = [3,6,6,8,8,7,7,9,8,8] # Goes from 10 to 19
    tens = [0,0,6,6,5,5,5,7,6,6] # Doesn't include 10
    
    # Start counting
    count = 0
    sNum = str(number)
    if len(sNum) == 4:
        return 11 # one thousand
    if len(sNum) > 1:
        if int(sNum[-2]) == 1:
            count += teens[int(sNum[-1])] # includes ones and tens place
        else:
            count += digits[int(sNum[-1])] # ones place
            count += tens[int(sNum[-2])] # tens place
    else:
        count += digits[int(sNum[0])] # ones place
    if len(sNum) > 2:
        count += digits[int(sNum[0])] + 7 # for 'hundred'
        if not ((sNum[1] == '0') and (sNum[2] == '0')):
            count += 3 # for 'and'
    return count

def rangeCount(maxValue):
    """
    Counts the total letters used in all numbers not greater than maxValue.
    Assumes maxValue will never be greater than 1000.
    """
    total = 0
    for i in range(1, maxValue + 1):
        total += countLetters(i)
    return total

# PROBLEM 11

def greatProduct():
    # Format the array properly
    f = open(filepath_base + "p11.txt")
    lines = f.readlines()
    arr = []
    for line in lines:
        arr.append(map(int,line.split()))
    # Start calculating
    biggest = 0
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            for i in range(4):
                product = prod(arr, r, c, i)
                biggest = max([biggest, product])
    return biggest

def prod(arr,r,c,flag):
    if flag == 0:
        if c + 3 > 19:
            return 0 # Out of bounds
        product = 1
        for i in range(4):
            product *= arr[r][c+i]
        return product
    elif flag == 1:
        if r + 3 > 19:
            return 0 # Out of bounds
        product = 1
        for i in range(4):
            product *= arr[r+i][c]
        return product
    elif flag == 2:
        if (r + 3 > 19) or (c - 3 < 0):
            return 0 # Out of bounds
        product = 1
        for i in range(4):
            product *= arr[r+i][c-i]
        return product
    else:
        if (r + 3 > 19) or (c + 3 > 19):
            return 0 # Out of bounds
        product = 1
        for i in range(4):
            product *= arr[r+i][c+i]
        return product

# PROBLEM 19

def sundays2(inp):
    """
    Returns the number of Sundays on the first day of a month between
    1 Jan 1900 and the 31 Dec of the input year.
    """
    count = 0
    for year in range(1901, inp):
        for month in range(1,13):
            time = datetime.date(year, month, 1)
            if time.weekday() == 6:
                count += 1
    return count

def sundays(inp):
    """
    Returns the number of Sundays on the first day of a month between
    1 Jan 1900 and the 31 Dec of the input year.
    """
    # Count Monday 1 Jan 1900 as day 1, so day % 7 == 0 on Sundays.
    # This means 1 Jan 1901 is day 366.
    count = 0
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = 1901
    month = 0
    day = 366
    while year <= inp:
        if day % 7 == 0:
            count += 1
        day += months[month]
        if leapYear(year) and month == 1:
            day += 1
        month += 1
        if month % 12 == 0:
            month = 0
            year += 1
    return count

def leapYear(year):
    """
    Returns true if the input year is a leap year.
    """
    if not year % 4 == 0:
        return False
    elif not year % 100 == 0:
        return True
    elif not year % 400 == 0:
        return False
    else:
        return True

# PROBLEM 34

def digitFac(num):
    """
    Returns true if the input is the sum of the factorials of its digits.
    """
    if num < 3:
        return False # 1!=1 and 2!=2 aren't sums
    digitFactorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    digitSum = 0
    for digit in str(num):
        digitSum += digitFactorials[int(digit)]
    return digitSum == num

"""
Let's say a factorion has 5 digits: _ _ _ _ _
The lowest possible number is 10000, or 10**4
The highest possible is 99999, or 9!*5
So if n is a factorion with d digits, 10**(d-1) <= n <= 9!*d

Running map(lambda x: (10**(x-1),factorial(9)*x), range(12)) shows that
this criterion is only going to be satisfied for d < 8, so no factorions
can have more than 7 digits.  Max possible is 9999999.

However, 9!*7 = 2540160, which is more restrictive than 9999999.
We clearly can't have a factorion greater than 2540160, which means that the
largest possible number would be 1999999.  However, this gives the sum of
2177281, which is too large, so we can't have six nines in the number.
This means that the next highest would be 1999998, which gives a sum of
1854721. Therefore we can't have numbers bigger than that as factorions.
"""

def findFactorions():
    """
    Returns all factorions in a list in ascending order. Excludes 1 and 2.
    """
    n = 0
    factorions = []
    while n < 1854722:
        if digitFac(n):
            factorions.append(n)
        n += 1
    return factorions


# PROBLEM 18 / 67

# Probably try a memoized recursive method starting from the bottom.

def loadTriangle():
    # Load triangle from file
    f = open(filepath_base + "p067_triangle.txt")
    lines = f.readlines()
    triArr = []
    memoArr = []
    for line in lines:
        proc_line = map(int, line.split())
        triArr.append(proc_line)
        memoArr.append([0]*len(proc_line))
    best = 0
    for n in range(len(triArr[-1])):
        result = findMaxPath(triArr, len(triArr)-1, n, memoArr)
        if result > best:
            best = result
    return best

def findMaxPath(triangle, r, c, memo):
    if c < 0 or c >= len(triangle[r]):
        return -1
    if r == 0:
        memo[r][0] = triangle[r][0]
        return triangle[r][0]
    if memo[r][c] > 0:
        return memo[r][c]
    else:
        left = findMaxPath(triangle,r-1,c-1,memo)
        right = findMaxPath(triangle,r-1,c,memo)
        result = triangle[r][c] + max(left,right)
        memo[r][c] = result
        return result

# PROBLEM 21

def amicable(maximum):
    """
    Returns the sum of all amicable numbers less than maximum.
    """
    memo = {}
    total = 0
    for n in range(1,maximum):
        d = divisor(n,1) - n
        if d >= maximum or d == n:
            continue
        memo[n] = d
        if d in memo and memo[d] == n:
            print "("+str(d)+","+str(n)+")"
            total += d
            total += n
    return total

# PROBLEM 22

def nameScores():
    # Import the name data
    f = open(filepath_base + "p022_names.txt")
    names = f.readline().strip('"').split('","')
    names.sort()
    # Set up letter scores
    letters = {}
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for letter in alphabet:
        letters[letter] = alphabet.index(letter)+1
    # Calculate name scores
    totalScore = 0
    for name in names:
        nameScore = 0
        for letter in name:
            nameScore += letters[letter]
        totalScore += nameScore*(names.index(name)+1)
    return totalScore

# PROBLEM 48

def lastDigits(maximum, numDigits):
    """
    Returns the last numDigits digits of the self-power sum up to maximum.
    E.g. 1^1 + 2^2 + 3^3 + ... + max^max
    """
    digitSum = 0
    for n in range(maximum):
        selfPower = (n+1)**(n+1)
        lastDigits = selfPower % 10**numDigits
        digitSum += lastDigits
    return digitSum % 10**numDigits

# PROBLEM 24

def nCr(n,r):
    """
    Returns the number of combinations of r objects from a set of n objects.
    """
    if r > n:
        return 0
    return factorial(n) / (factorial(r) * factorial(n - r))

def nPr(n,r):
    """
    Returns the number of permutations of r objects from a set of n objects.
    """
    if r > n:
        return 0
    return factorial(n) / factorial(n - r)

"""
We have a set of strings 10 characters long, made by arranging the digits 0-9
without repetition.  This means that there are nPr(10,10) = 3,628,800 strings
in the set.  There are nPr(9,9) = 362,880 strings which start with 0, nPr(9,9)
strings which start with 1, etc.  Therefore the lexicographic permutations are
split up so that #1 - #362880 start with 0, #362881 - #725760 start with 1, and
#725761 - #1088640 start with 2.  This means the millionth one starts with 2.

There are nPr(8,8) = 40320 strings for with two characters fixed.  We can use
this to determine that #725761 - #776080 start with 20, #776081 - #806400 start
with 21, #806401 - #846720 start with 23, #846721 - #887040 start with 24,
#887041 - #927360 start with 25, #927361 - #967680 start with 26, and #967681 -
#1008000 start with 27.

We can use this same method to refine down the number place by place.
"""

def lexicographic(i, chars):
    """
    Returns the ith lexicographic permutation of the input set.  Assumes chars
    is sorted with no repetition.
    """
    if i == 0:
        return
    n = len(chars)
    out = [0]*n
    position = 1
    for j in range(n):
        chars_index = (i - position) / nPr(n-1-j, n-1-j)
        out[j] = chars[chars_index]
        del chars[chars_index]
        position += nPr(n-1-j, n-1-j) * chars_index   
    return "".join(map(str, out))


