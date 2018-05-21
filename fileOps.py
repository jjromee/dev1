import os
import sys
def passFile(args):
    passed = True
    numArgs = len(args)
    if numArgs != 2:
       print "Please enter one file to read in"
       passed = False
       #exit(0)
    else:
        print "File read in is: ", str(args[1])

    #check if file exits within directory. If so, open. Else, terminate program.
    if not os.path.isfile(args[1]):
       print "Enter an existing file"
       passed = False
       #exit(0)
    return passed