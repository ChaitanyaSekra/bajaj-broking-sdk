from pydantic import BaseModel, Field
from datetime import datetime, UTC
import uuid
from app.models.order import OrderSide


class Trade(BaseModel):
    tradeId: str = Field(default_factory=lambda: str(uuid.uuid4()))
    orderId: str
    symbol: str
    side: OrderSide
    quantity: int
    price: float
    executedAt: datetime = Field(default_factory=lambda: datetime.now(UTC))
