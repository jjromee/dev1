#create list of each word in file
def listOfWords(file):
    words = file.read().split()
    if len(words) == 0 :
        print "File contains no values/words. Please try a new file. Exiting"
        exit(0)
    return words