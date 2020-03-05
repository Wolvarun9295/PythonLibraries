import mysql.connector

myDatabase = mysql.connector.connect(host="localhost", user="root", database="myDatabase")
myCursor = myDatabase.cursor()
myCursor.execute("Select * from employee")
myResult = myCursor.fetchall()

for row in myResult:
    print(row)
