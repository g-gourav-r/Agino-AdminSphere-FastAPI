import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Singleton pattern for MongoDB connection
client = None
db = None

def get_database():
    """Establish and return a MongoDB connection."""
    global client, db
    if client is None:
        MONGO_URI = os.getenv("MONGO_URI")
        MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DB_NAME]
    return db
