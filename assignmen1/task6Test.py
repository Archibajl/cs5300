import task6

def testCountWords():
    wordCount = task6.fileWordCount("task6_read_me.txt")
    assert wordCount == 115
