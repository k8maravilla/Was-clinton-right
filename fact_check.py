import csv

with open("information.txt", "r", encoding= "UTF8") as file:
    csvreader = csv.reader(file, delimiter= ",")
    for row in csvreader:
        print(','.join(row))