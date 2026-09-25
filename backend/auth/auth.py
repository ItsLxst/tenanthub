from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# make CryptContext object, specify we will use bcrypt

def hash_password(password: str) -> str:
    """ function that hashes a password using bcrypt """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """ function that verifies a password against the hashed passwrord """
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    """ function that creates a JWT access token """
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    copy_data = data.copy()
    copy_data.update({"exp": datetime.utcnow() + timedelta(minutes=30)})
    return jwt.encode(copy_data, SECRET_KEY, algorithm=ALGORITHM)