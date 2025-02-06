import pymongo # type: ignore

# creates a connection to MongoDB server
client = pymongo.MongoClient("mongodb+srv://arun_yeldi:0005@arun-yeldi.iymip.mongodb.net/?retryWrites=true&w=majority&appName=Arun-Yeldi")

# Select a database
db = client["department_db"]

# Access a collection
collection = db["employee"]

# Example: Insert a document
collection.insert_one({'temp':'hello'})

# Inserting a document
collection.insert_one({"name":"Arun", "ID":212})

# Example: Find documents
documents = collection.find()   
for doc in documents:
    print(doc)

# Close the connection
client.close()