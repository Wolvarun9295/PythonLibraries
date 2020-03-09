import pymongo
from bson import ObjectId

connection = pymongo.MongoClient("localhost:27017")
database = connection['myDB']
collection = database['people']
print("Database Connected!")
print()


def insert(data):
    document = collection.insert_one(data)
    return document.inserted_id


def update(document_id, data):
    document = collection.update_one({"_id": ObjectId(document_id)}, {"$set": data}, upsert=True)
    return document.acknowledged


def delete(document_id):
    document = collection.delete_one({"_id": ObjectId(document_id)})
    return document.acknowledged


def read():
    data = collection.find()
    return list(data)


# data = {'name': 'Golu'}
# insert(data)
# update('5e65d35ab171938550327480', data)
# delete('5e65d35ab171938550327480')
print(read())

connection.close()
print()
print('Connection Closed!')
