import mysql.connector

myDatabase = mysql.connector.connect(host="localhost", user="root", database="myDatabase")
myCursor = myDatabase.cursor()
sqlForm = "Insert into employee(name,salary) values(%s,%s)"
employees = [("Varun", 20000), ("Sandesh", 9300)]

myCursor.executemany(sqlForm, employees)

myDatabase.commit()
