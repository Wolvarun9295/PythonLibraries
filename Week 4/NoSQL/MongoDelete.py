from MongoConn import col

col.delete_one({"firstName": "Vivan"})
print("Deletion Successful!")
