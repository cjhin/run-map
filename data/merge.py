#!/usr/bin/python

import os, sys

path = "./"
dirs = os.listdir( path )

output = open('all.gpx', 'w')

output.write('<?xml version="1.0" encoding="UTF-8"?>')
output.write('<gpx>')

# This would print all the files and directories
for file in dirs:
    f = open(file, 'r')

    while True:
        line = f.readline()
        if line.startswith('<trkpt'):
            output.write(line)

        # end of file
        if len(line) < 2:
            break
    f.close()

output.write('</gpx>')
output.close()
