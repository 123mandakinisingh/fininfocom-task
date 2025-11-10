from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import fetch_all_orders

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.get("/")
def get_all_orders(db: Session = Depends(get_db)):
    return fetch_all_orders(db)
