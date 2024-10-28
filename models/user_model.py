from config.database import get_database
from bson import ObjectId

class UserModel:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db["users"]

    def get_all_users(self):
        """Fetch all users from the 'Users' collection."""
        users = self.collection.find()
        return [self._serialize_user(user) for user in users]

    def _serialize_user(self, user):
        """Convert MongoDB document to JSON serializable format."""
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
        return user
