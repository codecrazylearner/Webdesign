# TODO
import cs50
import csv
import sys


if len(sys.argv) != 2:
    sys.exit("missing command line arguments")

db = cs50.SQL("sqlite:///students.db")
with open("characters.csv", "r") as file:

    reader = csv.DictReader(file)
# Loop through rows
    for row in reader:
        names = row['name'].split()
        first,middle,last=names[0],names[1] if len(names)==3 else None,names[-1]
        house = row['house']
        birth = row['birth']
        db.execute("INSERT INTO students(first, middle, last, house, birth)VALUES(?, ?, ?, ?, ?)",
                   first, middle, last, row['house'], int(row['birth']))



#        if len(names) == 2:
#           first = names[0].strip()
#            last = names[1].strip()
#           db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
#                  first,None , last, row["house"], int(row["birth"]))

#        elif len(names) == 3:
#            first = names[0].strip()
#           middle = names[1].strip()
#          last = names[2].strip()
#            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
#                   first, middle, last, row["house"], int(row["birth"]))



