import sys

from wordList import listOfWords
from histogram import histo, sortHisto, printMe
from fileOps import passFile, outputFile

def main():
    """Reads in a file and generates a histogram of words
    used, sorted from most occurrences to least.
    Data is stored in output.txt
    """
    passed = passFile(sys.argv) #verify file exists
    if passed == False:
        exit(0)
    else:
        file = open(sys.argv[1], "r")   #open file
        words = listOfWords(file)       #make list based on words read in
        hist = histo(words)             #create dictionary with # occurrences
        sortedHist = sortHisto(hist)    #sort dictionary based on occurances
        outputFile(sortedHist)          #print formatted output to output file
        file.close()                    #close file

main()