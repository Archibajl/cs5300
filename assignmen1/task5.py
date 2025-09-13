
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


def listOfFavoriteBooks():
    return listOfBooks

def listOfThreeFavoriteBooks():
    return listOfBooks[0:3]

def getStudentDatabase():
    return studentDatabase