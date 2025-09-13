import task3

def testIsPositive():
    assert task3.isPositive(2)
    assert not task3.isPositive(-3)

def testIsNegative():
    assert task3.isNegative(-55)
    assert not task3.isNegative(7)

def testIsZero():
    assert task3.isZero(0)
    assert not task3.isZero(3)

# def testPrintPrimeNumbers(capsys):
#     firstTenPrimeNumbers = [3,5,7,11,13,17,23,27,31,37]
#     primeNumbers = task3.printPrimeNumbers(10)
#     out, _ = capsys.readouterr()
#     assert firstTenPrimeNumbers == primeNumbers
#     assert out == firstTenPrimeNumbers

def testSumFirstHundredNumbers():
    assert 5050 == task3.sumFirstHundredNumbers()
