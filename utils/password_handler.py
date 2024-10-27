from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    """Hash the password."""
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    """Verify a hashed password."""
    return pwd_context.verify(plain_password, hashed_password)
