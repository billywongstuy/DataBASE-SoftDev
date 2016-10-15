import csv

fObj = open("peeps.csv") 
d=csv.DictReader(fObj)

for row in d:
    insertion = "INSERT INTO students VALUES (\"" + row["name"] + "\", " + row["id"] + ")"
    print (insertion)

print ("\n\n\n")

fObj2 = open("courses.csv") 
d2=csv.DictReader(fObj2)

for row in d2:
    insertion = "INSERT INTO courses VALUES (\"%s\", %s, %s)" % (row["code"], row["id"], row["mark"])
    print (insertion)


    
