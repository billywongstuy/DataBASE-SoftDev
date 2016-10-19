import sqlite3

f = "info.db"

db = sqlite3.connect(f)
c = db.cursor()


'''q = "SELECT id FROM courses"
a = c.execute(q)
print a #for row in a:
   # print row[0]'''

def grades(id):
    q = "SELECT name FROM students WHERE id=%d" % (id)
    a = c.execute(q)
    for row in a:
        print "Student: " + row[0]
    q = "SELECT code,mark FROM courses WHERE id=%d" % (id)
    a = c.execute(q) #a should be a dictionary, why is it a cursor???????
    for row in a:
        print row[0] + ": " + str(row[1])


def average(id):
    q = "SELECT name FROM students WHERE id=%d" % (id)
    a = c.execute(q)
    for row in a:
        print "Student: " + row[0]
    q = "SELECT mark FROM courses WHERE id=%d" % (id)
    a = c.execute(q) #a should be a dictionary, why is it a cursor???????
    classNo = 0
    totalPts = 0
    for row in a:
        totalPts += row[0]
        classNo += 1
    print "Average: %d" % (totalPts/classNo)
    
        
grades(1)
average(1)
