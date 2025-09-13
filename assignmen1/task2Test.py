import task2

print(task2.divideInteger)
floatValue = task2.getFloat
print(floatValue)
# print("" + task2.inverseBooleanValue)


def testMultiplyFloat():
    floatValue = task2.getFloat(1)
    assert isinstance(floatValue, float)
    assert floatValue == 3.1435

def testDivideInteger():
    modInt = task2.divideInteger(3)
    assert isinstance(modInt, int)
    assert modInt == 333

def testConcatString():
    stringValue = task2.concatString()
    assert isinstance(stringValue, str)
    assert stringValue == "My String and my new string"

def testInverseBooleanValue():
    assert task2.inverseBooleanValue() == True

