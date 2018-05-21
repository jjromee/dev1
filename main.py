import sys
import os
import string

from wordList import listOfWords
from histogram import histo, sortHisto, printMe
from fileOps import passFile
def main():
    passed = passFile(sys.argv)
    if passed == False:
        exit(0)
    else:
        file = open(sys.argv[1], "r")
        words = listOfWords(file)
        #print words
        hist = histo(words)
        sortedHist = sortHisto(hist)
        printMe(sortedHist)
        file.close()

main()