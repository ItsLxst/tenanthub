from datetime import datetime, timezone
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database.database import get_db
from database.models import Organization, Membership, User
from auth.dependencies import get_current_user

router = APIRouter()

class CreateOrganizationRequest(BaseModel):
    name: str
    description: str | None = None

@router.post("/")
def create_organization(request: CreateOrganizationRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    now = datetime.now(timezone.utc)

    new_organization = Organization(
        name=request.name,
        description=request.description,
        created_at=now,
        updated_at=now
    )
    db.add(new_organization)
    db.flush()

    new_membership = Membership(
        user_id=current_user.user_id,
        organization_id=new_organization.organization_id,
        role="owner",
        status="active",
        joined_at=now,
        created_at=now,
        updated_at=now
    )
    db.add(new_membership)
    db.commit()

    return {
        "organization_id": new_organization.organization_id,
        "name": new_organization.name,
        "role": "owner"
    }