import sys
import os
import string

from wordList import listOfWords
from histogram import histo, sortHisto, printMe
from fileOps import passFile, outputFile
def main():
    passed = passFile(sys.argv)
    if passed == False:
        exit(0)
    else:
        file = open(sys.argv[1], "r")
        words = listOfWords(file)
        hist = histo(words)
        sortedHist = sortHisto(hist)
        outputFile(sortedHist)
        file.close()

main()