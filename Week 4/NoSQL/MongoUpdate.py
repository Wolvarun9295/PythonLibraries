from MongoConn import col

col.update_one({"firstName": "Yug"}, {"$set": {"firstName": "John"}})
print("Update Operation Successful!")
