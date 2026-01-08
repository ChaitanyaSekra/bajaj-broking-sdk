from typing import Dict
from app.models.portfolio import PortfolioItem
from app.repositories.trade_store import get_all_trades
from app.repositories.instrument_store import get_all_instruments
from app.models.order import OrderSide


def calculate_portfolio():
    trades = get_all_trades()
    instruments = {i.symbol: i for i in get_all_instruments()}

    portfolio: Dict[str, Dict] = {}

    for trade in trades:
        symbol = trade.symbol

        if symbol not in portfolio:
            portfolio[symbol] = {
                "quantity": 0,
                "totalCost": 0.0
            }

        if trade.side == OrderSide.BUY:
            portfolio[symbol]["quantity"] += trade.quantity
            portfolio[symbol]["totalCost"] += trade.quantity * trade.price

        elif trade.side == OrderSide.SELL:
            portfolio[symbol]["quantity"] -= trade.quantity
            portfolio[symbol]["totalCost"] -= trade.quantity * trade.price

    result = []

    for symbol, data in portfolio.items():
        quantity = data["quantity"]

        if quantity == 0:
            continue  # no holding

        avg_price = data["totalCost"] / quantity
        ltp = instruments[symbol].lastTradedPrice
        current_value = quantity * ltp

        result.append(
            PortfolioItem(
                symbol=symbol,
                quantity=quantity,
                averagePrice=round(avg_price, 2),
                currentValue=round(current_value, 2)
            )
        )

    return result
