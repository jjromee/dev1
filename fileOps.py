import os
import sys
from histogram import printMe
def passFile(args):
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
    output = open("output.txt","w")
    sys.stdout = output
    printMe(sortedHistogram)
    sys.stdout = sys.__stdout__
    output.close