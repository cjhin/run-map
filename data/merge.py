#!/usr/bin/python

# Take all .gpx files in this directory
# and merge them into one large file

import os
import re

path = "./"
dirs = os.listdir( path )

output = open('all.gpx', 'w')

# header for the gpx xml file
output.write('<?xml version="1.0" encoding="UTF-8"?>')
output.write('<gpx>')

for file in dirs:
    if file.endswith('.gpx') and file != 'all.gpx':
        f = open(file, 'r')

        while True:
            line = f.readline()
            # only write the <trkpt tags
            if line.startswith('<trkpt'):
                new_line = re.sub(r'(?is)<ele>.+</time>', '', line)
                output.write(new_line)

            # end of file
            if len(line) < 2:
                break
        f.close()
    elif file.endswith('.tcx'):
        f = open(file, 'r')

        while True:
            line = f.readline()
            if line.strip().startswith('<LatitudeDegrees'):
                curr_lat = line[line.index('>')+1:line.index('</')]
                line = f.readline()
                curr_lon = line[line.index('>')+1:line.index('</')]
                str_to_write = '<trkpt lat="' + curr_lat + '" lon="' + curr_lon + '"></trkpt>\n'
                output.write(str_to_write)

            # end of file
            if len(line) < 2:
                break
        f.close()

output.write('</gpx>')
output.close()
