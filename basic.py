import sqlite3

f = "info.db"

db = sqlite3.connect(f)
c = db.cursor()


'''q = "SELECT id FROM courses"
a = c.execute(q)
print a #for row in a:
   # print row[0]'''

def grades(id):
    q = "SELECT mark FROM courses WHERE id=" + str(id)
    a = c.execute(q) #a should be a dictionary, why is it a cursor???????
    marks = a
    for row in marks:
        print marks[0]

grades(1)
