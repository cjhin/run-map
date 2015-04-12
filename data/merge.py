#!/usr/bin/python

# Take all .gpx files in this directory
# and merge them into one large file

import os

path = "./"
dirs = os.listdir( path )

output = open('all.gpx', 'w')

# header for the gpx xml file
output.write('<?xml version="1.0" encoding="UTF-8"?>')
output.write('<gpx>')

for file in dirs:
    if file != 'all.gpx':
        f = open(file, 'r')

        while True:
            line = f.readline()
            # only write the <trkpt tags
            if line.startswith('<trkpt'):
                output.write(line)

            # end of file
            if len(line) < 2:
                break
        f.close()

output.write('</gpx>')
output.close()
