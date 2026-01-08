from typing import Dict
from app.models.order import Order

ORDERS: Dict[str, Order] = {}

def save_order(order: Order):
    ORDERS[order.orderId] = order
    return order

def get_order(order_id: str) -> Order | None:
    return ORDERS.get(order_id)
