from fastapi import APIRouter
from app.services.portfolio_service import calculate_portfolio

router = APIRouter(prefix="/api/v1/portfolio", tags=["Portfolio"])

@router.get("")
def fetch_portfolio():
    return calculate_portfolio()
