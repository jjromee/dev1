import string

def histo(words):
    """Takes in list of words and creates histogram while taking away punctuation and
    whitespace.
    Args:
        words: list of words
    Return:
        hist: dictionary of words with number of occurrences"""
    hist = {}
    for word in words:
      word = word.lower()  #set to lowercase to increment count with same word no matter punctuation
      word = word.strip(string.punctuation + string.whitespace) #take away any punctuation or whitespace for accuracy
      hist[word] = hist.get(word, 0) + 1 #count number of occurrences of word, if zero, increments by one, else increment previous num by 1
    return hist


def sortHisto(hist):
    """Takes in dictionary and sorts from greatest occurrence to least
    Args:
        hist - unsorted histogram dictionary
    Return:
        sorted histogram dictionary"""
    sortedHist = sorted(hist.items(), key = lambda x: x[1], reverse = True)
    return sortedHist

def printMe(sortedHist):
    """Print passed in data in specific format: i.e. the | === (3)
    Args:
        sortedHist - sorted histogram dictionary
    Return:
        Printed data"""
    for word, value in sortedHist:
        print word, '|', ('=' * value), '({})'.format(value)