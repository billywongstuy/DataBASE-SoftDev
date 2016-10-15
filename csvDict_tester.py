import csv

fObj = open("peeps.csv") 
d=csv.DictReader(fObj)

for k in d:
    print k
    
