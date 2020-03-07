from MongoConn import col

col.insert_one(
    {
        "firstName": "Varun",
        "lastName": "Nagrare",
        "salary": 20000
    }
)

col.insert([{"firstName": "Vivan", "lastName": "Phulke", "status": "pending", "salary": 10000},
            {"firstName": "Yug", "lastName": "Ingle", "status": "missing"}])

print("Insertion Successful!")
