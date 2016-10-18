import sqlite3

f = "info.db"

db = sqlite3.connect(f)
c = db.cursor()


'''q = "SELECT id FROM courses"
a = c.execute(q)
print a #for row in a:
   # print row[0]'''

def grades():
    q = "SELECT name, id from students"
    a = c.execute(q) #a should be a dictionary, why is it a cursor???????/ 
    print a #??????
    for row in a:
        print row[1] 
    #print q

grades()
