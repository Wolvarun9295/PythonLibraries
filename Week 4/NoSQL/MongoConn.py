from pymongo import MongoClient

try:
    client = MongoClient('localhost', 27017)
    db = client.myData
    col = db.people
    print("Connection Successful!")
except Exception:
    print("Connection Failed!")
