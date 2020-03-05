import mysql.connector

myDatabase = mysql.connector.connect(host="localhost", user="root")
myCursor = myDatabase.cursor()
myCursor.execute("Create database myDatabase")

for tb in myCursor:
    print(tb)
