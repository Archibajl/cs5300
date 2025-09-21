import task4

def testDiscountedPrices():
    assert 75 == task4.calculate_discount(100, 25)
    assert 350 == task4.calculate_discount(500, 30)
    assert 510 == task4.calculate_discount(600, 15)

def testDiscountedPricesFloat():
    assert 96.42 == task4.calculate_discount(425.33, 77.33)

def testDiscountedPricesMissMatched():
    assert 405.75 == task4.calculate_discount(724.55, 44)
    assert 266.76 == task4.calculate_discount(1200, 77.77)