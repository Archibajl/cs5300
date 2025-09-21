import re

#Reads in file given in argument then calls count
def fileWordCount(filename):
    with open(filename, 'r') as file:
        text = file.read()
        return countWords(text)

# removes all non alpha numeric characters and splits the text into tokens
# then returns the count of tokens
def countWords(text):
    #Replaces non alpha numeric characters with null characters
    text.replace(',', '')
    text.replace(',', '')
    tokens = text.split(" ")
    return len(tokens)

