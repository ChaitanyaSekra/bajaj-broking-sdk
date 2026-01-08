from fastapi import APIRouter
from app.repositories.instrument_store import get_all_instruments

router = APIRouter(prefix="/api/v1/instruments", tags=["Instruments"])

@router.get("")
def fetch_instruments():
    return get_all_instruments()
