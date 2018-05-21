def listOfWords(file):
    """Create list of each word in given file
    Args:
        file - file being read in
    Return:
        words - list of words in file given"""
    words = file.read().split()
    if len(words) == 0 :
        print "File contains no values/words. Please try a new file. Exiting"
        exit(0)
    return words