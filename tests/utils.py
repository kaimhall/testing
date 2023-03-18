from pymongo import MongoClient


def call_db():
    client = MongoClient(
        "mongodb+srv://kaimhall:t-Y5gQwYDeB2VbT@testingmydb.nl4ym8m.mongodb.net/?retryWrites=true&w=majority"
    )
    db = client.testingmydb
    return db


print(call_db())
