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
        
def sumFirstHundredNumbers():
    sum = 0
    for i in range(101):
        sum += i
    return sum