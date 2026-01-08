from app.models.trade import Trade
from app.models.order import Order
from app.repositories.trade_store import save_trade
from app.repositories.instrument_store import get_all_instruments


def create_trade_from_order(order: Order) -> Trade:
    instruments = {i.symbol: i for i in get_all_instruments()}
    instrument = instruments[order.symbol]

    trade = Trade(
        orderId=order.orderId,
        symbol=order.symbol,
        side=order.side,
        quantity=order.quantity,
        price=instrument.lastTradedPrice
    )

    save_trade(trade)
    return trade
