from models.admin_model import AdminModel
from utils.jwt_handler import create_access_token

class AdminController:
    def __init__(self):
        self.admin_model = AdminModel()

    def register_admin(self, username: str, email: str, password: str):
        if self.admin_model.get_admin_by_email(email):
            return {"error": "Admin with this email already exists"}
        self.admin_model.create_admin(username, email, password)
        return {"message": "Admin account created successfully"}

    def login_admin(self, email: str, password: str):
        admin = self.admin_model.verify_admin_credentials(email, password)
        if not admin:
            return {"error": "Invalid email or password"}
        # Generate JWT token
        token = create_access_token({"sub": email})
        return {"access_token": token, "token_type": "bearer"}
