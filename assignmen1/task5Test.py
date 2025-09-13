import task5

def testListOfFavoriteBooks():
    listOfBooks = task5.listOfFavoriteBooks()
    assert len(listOfBooks) == 8
    assert listOfBooks[0] == "Three Body Problem, XiXen Liu"

def testListOfThreeFavoriteBooks():
    listOfBooks = task5.listOfThreeFavoriteBooks()
    assert len(listOfBooks) == 3

def testStudentDatabase():
    studentDatabase = task5.getStudentDatabase()
    assert len(studentDatabase) == 5
    assert studentDatabase["Alice Johnson"] == "S1001"
    assert studentDatabase["Brian Lee"] == "S1002"
    assert studentDatabase["Carla Gomez"] == "S1003"
    assert studentDatabase["David Kim"] == "S1004"
    assert studentDatabase["Emily Zhang"] == "S1005"
