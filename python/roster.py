# TODO

import cs50
import csv
import sys
from sys import argv


if len(sys.argv) != 2:
    sys.exit("missing command line arguments")
db = cs50.SQL("sqlite:///students.db")
rows=db.execute('SELECT distinct first,middle,last,birth FROM STUDENTS WHERE house = ? ORDER BY last,first',argv[-1])
for row in rows:
    print(row['first'] + ' ' + (row['middle'] if row['middle'] else ' ' )+ ' '+ row['last'] +', born' +str(row['birth']))
