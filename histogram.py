import string

#create histogram dictionary holding word and number of occurrences
def histo(words):
    hist = {}
    for word in words:
      word = word.lower()  #set to lowercase to increment count with same word no matter punctuation
      word = word.strip(string.punctuation + string.whitespace) #take away any punctuation or whitespace for accuracy
      hist[word] = hist.get(word, 0) + 1 #count number of occurrences of word, if zero, increments by one, else increment previous num by 1
    return hist


#takes in dictionary and sorts from greatest value to least
def sortHisto(hist):
    sortedHist = sorted(hist.items(), key = lambda x: x[1], reverse = True)
    return sortedHist

#print the word followed by a pipe character ("|"),
#a number of equal signs that are proportional to the
#number of occurrences found in the text, and the number of occurrences itself.
def printMe(sortedHist):
    for word, value in sortedHist:
        print word, '|', ('=' * value), '({})'.format(value)