from pymongo import MongoClient
from dotenv import load_dotenv  # Ensure this is imported correctly
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve MongoDB URI and Database Name from environment variables
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

# Initialize MongoDB client and database
client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

def get_admin_collection():
    return db["admins"]
