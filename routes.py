from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas
from utils import calculate_summary
from auth import require_roles
router = APIRouter()

# =========================
# 👤 USER APIs
# =========================

# Create User
@router.post("/users", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    # check if email exists
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    if user.role not in ["admin", "analyst", "viewer"]:
         raise HTTPException(status_code=400, detail="Invalid role")
    new_user = models.User(
        name=user.name,
        email=user.email,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# Get all users
@router.get("/users", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


# =========================
# RECORD APIs
# =========================
from auth import require_roles
# Create Record
@router.post("/records", response_model=schemas.RecordResponse)
def create_record(
    record: schemas.RecordCreate,
    db: Session = Depends(get_db),
    user=Depends(require_roles(["admin"]))  #ONLY ADMIN
):
    if record.type not in ["income", "expense"]:
        raise HTTPException(status_code=400, detail="Invalid type")

    # check if user exists
    user = db.query(models.User).filter(models.User.id == record.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_record = models.Record(
        amount=record.amount,
        type=record.type,
        category=record.category,
        date=record.date,
        note=record.note,
        user_id=record.user_id
    )

    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return new_record


@router.get("/records")
def get_records(
    db: Session = Depends(get_db),
    type: str = None,
    category: str = None
):
    query = db.query(models.Record)

    if type:
        query = query.filter(models.Record.type == type)

    if category:
        query = query.filter(models.Record.category == category)

    return query.all()

# Delete record
@router.delete("/records/{record_id}")
def delete_record(
    record_id: int,
    db: Session = Depends(get_db),
    user=Depends(require_roles("admin"))  # ONLY ADMIN
):
    record = db.query(models.Record).filter(models.Record.id == record_id).first()

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    db.delete(record)
    db.commit()

    return {"message": "Record deleted successfully"}


from auth import require_roles

@router.get("/summary")
def get_summary(
    db: Session = Depends(get_db),
    user_id: int = None,
    user=Depends(require_roles(["admin", "analyst"]))  # 🔥 BOTH allowed
):
    records = db.query(models.Record).all()
    return calculate_summary(records)