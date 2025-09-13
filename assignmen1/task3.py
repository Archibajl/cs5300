import math

def isPositive(value):
    if(value > 0):
        return True
    return False

def isNegative(value):
    if(value<0):
        return True
    False

def isZero(value):
    if(value == 0):
        return True
    return False
""" Determiens prime numbers for how ever many prime numbers you want to get
 Uses square root efficency improvement, tests all numbers before
 the root of the origional number.
 This works because all numbers 
 after the root must be multiplied by one that comes before the root in order to be 
equal to or less than the orrigional number.
"""
def printPrimeNumbers(numberOfPrimes):
    primeNumbers = [1]
    i=2
    while len(primeNumbers) < numberOfPrimes:
        isPrime = True
        for j in range(2, int(math.sqrt(i))+1):
            if(i%j != 0):
                isPrime = False
        if(isPrime):
            primeNumbers.append(i)
            print(i)
        i += 1

    return primeNumbers
        
#Counts and summs all numbers from 0 to 100
def sumFirstHundredNumbers():
    sum = 0
    for i in range(101):
        sum += i
    return sum