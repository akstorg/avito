import csv

with open('firm1.csv') as file:
    r = csv.readline(file)
    for raw in r:
        print(raw)