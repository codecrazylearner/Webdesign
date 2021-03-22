import csv

with open('input.txt') as csvfile:
   csv_reader = csv.DictReader(csvfile)
   for row in reader:
       print(row['Number'])