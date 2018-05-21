import sys
import os
import string
from wordList import listOfWords
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
        hist = {}
        for word in words:
            word = word.lower() #set to lowercase to increment count with same word no matter punctuation
            word = word.strip(string.punctuation + string.whitespace) #take away any punctuation or whitespace for accuracy
            hist[word] = hist.get(word, 0) + 1 #count number of occurrences of word, if zero, increments by one, else increment previous num by 1
        print hist
        sortedHist = sorted(hist.items(), key = lambda x: x[1], reverse = True)
        print sortedHist
        file.close()

main()