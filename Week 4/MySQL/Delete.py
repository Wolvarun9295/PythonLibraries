import mysql.connector

myDatabase = mysql.connector.connect(host="localhost", user="root", database="myDatabase")

myCursor = myDatabase.cursor()

sql = "delete from employee where salary=20000"
myCursor.execute(sql)
myDatabase.commit()
