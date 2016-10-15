import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="info.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

'''
q = "CREATE TABLE students (name TEXT, id INTEGER)"
c.execute(q)    #run SQL query
q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"
c.execute(q)
'''


q = "CREATE TABLE students (name TEXT, id INTEGER)"
c.execute(q);

with open("peeps.csv") as file:
    d = csv.DictReader(file)
    for row in d:
        insertion = "INSERT INTO students VALUES (%s, %i)" % (row["name"], int(row["id"]))
        c.execute(insertion)


r = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"
c.execute(r);


with open("courses.csv") as file:
    d = csv.DictReader(file)
    for row in d:
        insertion = "INSERT INTO courses VALUES (%s, %i, %i)" % (row["course"], int(row["id"]), int(row["mark"]))
        c.execute(insertion)


#==========================================================
db.commit() #save changes
db.close()  #close database
