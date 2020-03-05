import mysql.connector

myDatabase = mysql.connector.connect(host="localhost", user="root", database="classicmodels")
print(myDatabase)

if myDatabase:
    print("Connection Successful!")
else:
    print("Connection Failed!")
