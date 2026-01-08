from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional
from datetime import datetime, UTC
import uuid


class OrderSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderType(str, Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"


class OrderStatus(str, Enum):
    NEW = "NEW"
    PLACED = "PLACED"
    EXECUTED = "EXECUTED"
    CANCELLED = "CANCELLED"


class Order(BaseModel):
    orderId: str = Field(default_factory=lambda: str(uuid.uuid4()))
    symbol: str
    side: OrderSide
    orderType: OrderType
    quantity: int
    price: Optional[float] = None
    status: OrderStatus = OrderStatus.NEW
    createdAt: datetime = Field(default_factory=lambda: datetime.now(UTC))
