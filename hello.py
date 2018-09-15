import csv

with open("a.csv", 'w', newline='') as c:
    writer = csv.writer(c)
    writer.writerow("hi")