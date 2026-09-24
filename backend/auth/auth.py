from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# make CryptContext object, specify we will use bcrypt

def hash_password(password: str) -> str:
    """ function that hashes a password using bcrypt """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """ function that verifies a password against the hashed passwrord """
    return pwd_context.verify(plain_password, hashed_password)