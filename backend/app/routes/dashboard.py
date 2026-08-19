from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.dashboard_service import get_dashboard
from app.utils.dependencies import get_current_user

router = APIRouter()


@router.get("/dashboard")
def dashboard(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_dashboard(db)