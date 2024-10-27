from config.database import get_database
from utils.password_handler import hash_password, verify_password

class AdminModel:
    def __init__(self):
        self.collection = get_database()["admins"]

    def create_admin(self, username: str, email: str, password: str):
        """Create a new admin in the database."""
        hashed_password = hash_password(password)
        return self.collection.insert_one({
            "username": username,
            "email": email,
            "password": hashed_password
        })

    def get_admin_by_email(self, email: str):
        """Retrieve admin by email."""
        return self.collection.find_one({"email": email})

    def verify_admin_credentials(self, email: str, password: str):
        """Verify admin credentials for login."""
        admin = self.get_admin_by_email(email)
        if admin and verify_password(password, admin["password"]):
            return admin
        return None
