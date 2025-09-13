import task2

print(task2.modulusInteger)
floatValue = task2.getFloat
print(floatValue)
# print("" + task2.inverseBooleanValue)


def testMultiplyFloat():
    floatValue = task2.getFloat
    assert isinstance(floatValue, float)
    assert floatValue == 3.14

def testModulusInteger():
    modInt = task2.modulusInteger
    assert isinstance(modInt, int)
    assert modInt == 333

def testConcatString():
    assert task2.concatString() == "My String and my new string"

def testInverseBooleanValue():
    assert task2.inverseBooleanValue() == True

