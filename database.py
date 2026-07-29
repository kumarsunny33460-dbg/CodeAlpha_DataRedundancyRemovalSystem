from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

client = MongoClient(MONGO_URI)

db = client[DATABASE_NAME]

collection = db[COLLECTION_NAME]


def get_all_records():
    return list(collection.find())


def insert_record(record):
    collection.insert_one(record)


def find_duplicate(email, phone):

    return collection.find_one(
        {
            "$or": [
                {"email": email},
                {"phone": phone}
            ]
        }
    )


def get_record(record_id):

    return collection.find_one(
        {
            "_id": ObjectId(record_id)
        }
    )


def update_record(record_id, data):

    collection.update_one(
        {
            "_id": ObjectId(record_id)
        },
        {
            "$set": data
        }
    )


def delete_record(record_id):

    collection.delete_one(
        {
            "_id": ObjectId(record_id)
        }
    )


def total_records():

    return collection.count_documents({})