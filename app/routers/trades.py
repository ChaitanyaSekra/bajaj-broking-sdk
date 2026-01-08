from fastapi import APIRouter
from app.repositories.trade_store import get_all_trades

router = APIRouter(prefix="/api/v1/trades", tags=["Trades"])

@router.get("")
def fetch_trades():
    return get_all_trades()
