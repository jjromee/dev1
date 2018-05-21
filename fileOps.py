import os
import sys
from histogram import printMe
def passFile(args):
    """Verifies one file has been passed through and exists
    Args:
        args: the arguments passed in which contains the program name and file used
    Return:
        True or False depending on requirements met
        """
    passed = True
    numArgs = len(args)
    #must include two args (one being the program name) in order to continue
    if numArgs != 2:
       print "Please enter one file to read in"
       passed = False

    #check if file exits within directory. If so, open. Else, terminate program.
    if not os.path.isfile(args[1]):
        print "Enter an existing file"
        passed = False
    return passed

def outputFile(sortedHistogram):
    """Opens an output file where a sorted histogram is printed by redirecting stdout
    Args:
        sortedHistogram: dictionary containing the words and # of occurrences for each word
    Return:
        output.txt is altered with histogram"""
    output = open("output.txt","w")
    sys.stdout = output
    printMe(sortedHistogram)
    sys.stdout = sys.__stdout__
    output.close