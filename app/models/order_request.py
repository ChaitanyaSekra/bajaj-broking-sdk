from pydantic import BaseModel
from app.models.order import OrderSide, OrderType
from typing import Optional


class OrderRequest(BaseModel):
    symbol: str
    side: OrderSide
    orderType: OrderType
    quantity: int
    price: Optional[float] = None
