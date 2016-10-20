import sqlite3

f = "info.db"

db = sqlite3.connect(f)
c = db.cursor()


#SINGLE STUDENT FUNCTIONS
def grades(id):
    q = "SELECT name FROM students WHERE id=%d" % (id)
    a = c.execute(q)
    for row in a:
        print ("Student: " + row[0])
    q = "SELECT code,mark FROM courses WHERE id=%d" % (id)
    a = c.execute(q) 
    for row in a:
        print (row[0] + ": " + str(row[1]))


def average(id):
    q = "SELECT name FROM students WHERE id=%d" % (id)
    a = c.execute(q)
    for row in a:
        print ("Student: " + row[0])
    q = "SELECT mark FROM courses WHERE id=%d" % (id)
    a = c.execute(q) 
    classNo = 0
    totalPts = 0
    for row in a:
        totalPts += row[0]
        classNo += 1
    print ("Average: %d" % (totalPts/classNo))


def displayStudent(id):
    q = "SELECT name FROM students WHERE id=%d" % (id)
    a = c.execute(q)
    for row in a:
        print ("Student: " + row[0])
    print ("ID: " + str(id))
    q = "SELECT mark FROM courses WHERE id=%d" % (id)
    a = c.execute(q) 
    classNo = 0
    totalPts = 0
    for row in a:
        totalPts += row[0]
        classNo += 1
    print ("Average: %d" % (totalPts/classNo))
    
#grades(1)
#average(1)
#displayStudent(1)


#MULTI STUDENT FUNCTIONS

def allGrades():
    q = "SELECT name,id FROM students"
    c.execute(q)
    peepies = c.fetchall()
    for peep in peepies:
        q = "SELECT code,mark from courses WHERE id=%d" % (peep[1])
        a = c.execute(q)
        output = peep[0]
        for clas in a:
            output += " | %s : %d" %(clas[0],clas[1])
        print (output)


def averageAll():
    q = "SELECT name,id FROM students"
    c.execute(q)
    peepies = c.fetchall()
    for peep in peepies:
        q = "SELECT mark from courses WHERE id=%d" % (peep[1])
        a = c.execute(q)
        output = peep[0] + " | Average: "
        totalPts = 0
        noClasses = 0
        for clas in a:
            totalPts += clas[0]
            noClasses += 1
        output += str(round(totalPts/noClasses,1))
        print (output)
        
    
def displayStudentAll():
    q = "SELECT name,id FROM students"
    c.execute(q)
    peepies = c.fetchall()
    for peep in peepies:
        q = "SELECT mark from courses WHERE id=%d" % (peep[1])
        a = c.execute(q)
        output = peep[0] + " | Id: %d | Average: " % (peep[1])
        totalPts = 0
        noClasses = 0
        for clas in a:
            totalPts += clas[0]
            noClasses += 1
        output += str(round(totalPts/noClasses,1))
        print (output)

displayStudentAll()
