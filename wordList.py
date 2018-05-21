import sys

#create list of each word in file
def listOfWords(file):
    words = file.read().split()
    return words