import sys
import os
import string

from wordList import listOfWords
from histogram import histo, sortHisto
def main():
    #check number of arguments includes one file.
    numArgs = len(sys.argv)
    if numArgs != 2:
        print "Please enter one file to read in"
        exit(0)
    else:
        print "File read in is: ", str(sys.argv[1])

    #check if file exits within directory. If so, open. Else, terminate program.
    if not os.path.isfile(sys.argv[1]):
        print "Enter an existing file"
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