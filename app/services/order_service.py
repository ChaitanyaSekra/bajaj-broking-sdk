from fastapi import HTTPException, status
from app.models.order import Order, OrderStatus, OrderType
from app.models.order_request import OrderRequest
from app.repositories.order_store import save_order, get_order
from app.repositories.instrument_store import get_all_instruments
from app.services.trade_service import create_trade_from_order



def place_order(order_req: OrderRequest) -> Order:
    if order_req.quantity <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Quantity must be greater than zero"
        )

    if order_req.orderType == OrderType.LIMIT and order_req.price is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Price is mandatory for LIMIT orders"
        )

    instruments = {i.symbol: i for i in get_all_instruments()}
    if order_req.symbol not in instruments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Instrument not found"
        )

    order = Order(
        symbol=order_req.symbol,
        side=order_req.side,
        orderType=order_req.orderType,
        quantity=order_req.quantity,
        price=order_req.price,
        status=OrderStatus.PLACED
    )

    # Market orders execute immediately (simulation)
    if order.orderType == OrderType.MARKET:
        order.status = OrderStatus.EXECUTED
        create_trade_from_order(order)

    save_order(order)
    return order


def fetch_order(order_id: str) -> Order:
    order = get_order(order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return order
