#!/usr/bin/python

import os

# Open a file
fo = open("input.txt", "rw+")
fo1 = open("output.txt", "rw+")
print "Name of the file: ", fo.name
fo1.readlines()

line = fo.readline()
while line:
    print "Read Line: %s" % (line)
    os.system("megadl " + "'" + line + "'")
    line = fo.readline()
    fo1.write(line)

fo.close()
fo1.close()
os.system("rm input.txt")
os.system("touch input.txt")
