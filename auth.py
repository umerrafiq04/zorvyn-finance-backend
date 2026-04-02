from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models

# simulate current user (for now)
def get_current_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# role checker
def require_roles(allowed_roles: list):
    def checker(user_id: int, db: Session = Depends(get_db)):
        user = get_current_user(user_id, db)

        if user.role not in allowed_roles:
            raise HTTPException(status_code=403, detail="Access denied")

        return user
    return checker