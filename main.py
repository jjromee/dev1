import sys
import os
import string

from wordList import listOfWords
from histogram import histo, sortHisto
from fileOps import passFile
def main():
    passed = passFile(sys.argv)
    if passed == False:
        exit(0)
    else:
        file = open(sys.argv[1], "r")
        words = listOfWords(file)
        print words
        #create histogram dictionary holding word and number of occurrences
        hist = histo(words)
        print hist
        sortedHist = sortHisto(hist)
        print sortedHist

        file.close()

main()