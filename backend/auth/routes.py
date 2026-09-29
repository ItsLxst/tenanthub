from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database.database import get_db
from database.models import User
from auth.auth import hash_password

router = APIRouter()

# Define a Pydantic model for user registration


# Endpoint register