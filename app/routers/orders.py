from fastapi import APIRouter
from app.models.order_request import OrderRequest
from app.services.order_service import place_order, fetch_order

router = APIRouter(prefix="/api/v1/orders", tags=["Orders"])

@router.post("")
def create_order(order_request: OrderRequest):
    return place_order(order_request)

@router.get("/{order_id}")
def get_order(order_id: str):
    return fetch_order(order_id)
