import csv

items = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]] 

with open("chal9_3.csv", "w", newline = '') as f:
    for item in items:
        w = csv.writer(f, delimiter = ",")
        w.writerow(item)

with open("chal9_3.csv", "r") as f:
    r = csv.reader(f, delimiter = ",")
    for row in r:
        print(",".join(row))