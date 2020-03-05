import mysql.connector

myDatabase = mysql.connector.connect(host="localhost", user="root", database="myDatabase")

myCursor = myDatabase.cursor()

sql = "update employee set salary=70000 where name='Varun'"
myCursor.execute(sql)

myDatabase.commit()
