from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import User
import os

def get_current_user():
    pass


def require_role():
    pass

# TODO: Objective: 
# TODO: To establish a mechanism that verifies 
# TODO: "who this really is" and "what role they have in this organization" 
# TODO: when a user submits their token.
# TODO: also check if you missed any important imports.