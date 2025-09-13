
listOfBooks = ["Three Body Problem, XiXen Liu", "Dark Forrest, XiXen Liu", "Dune, Herbert", "SuperIntelligence, Nick Bostrom",
            "Fooled By Randomness, Taleb", "The Intelligent Investor, Grahm ", 
            "NeuroMancer, Gibson", "Do Androids Dream of Electric Sheep, Dick"]

studentDatabase = {
    "Alice Johnson": "S1001",
    "Brian Lee": "S1002",
    "Carla Gomez": "S1003",
    "David Kim": "S1004",
    "Emily Zhang": "S1005"
}

#returns list of books
def listOfFavoriteBooks():
    return listOfBooks

#returns first 3 in list of books
def listOfThreeFavoriteBooks():
    return listOfBooks[0:3]

#returns student Database (dictionary)
def getStudentDatabase():
    return studentDatabase