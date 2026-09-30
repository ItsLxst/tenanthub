from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database.database import get_db
from database.models import User
from auth.auth import hash_password

router = APIRouter()

# Define a Pydantic model for user registration
class RegisterRequest(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str

# Endpoint register
@router.post("/register")
def register_user(request: RegisterRequest, db: Session = Depends(get_db)):
    """ register a new user to database """
    # Check if user exists
    existing_user = db.query(User).filter(User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # If there is no user, create new one.
    new_user = User(
        email=request.email,
        password=hash_password(request.password),
        first_name=request.first_name,
        last_name=request.last_name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully", "user_id": new_user.user_id, "email": new_user.email}