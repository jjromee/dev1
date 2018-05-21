import string


def histo(words):
    hist = {}
    for word in words:
      word = word.lower()  #set to lowercase to increment count with same word no matter punctuation
      word = word.strip(string.punctuation + string.whitespace) #take away any punctuation or whitespace for accuracy
      hist[word] = hist.get(word, 0) + 1 #count number of occurrences of word, if zero, increments by one, else increment previous num by 1
    return hist
