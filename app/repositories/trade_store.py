from typing import List
from app.models.trade import Trade

TRADES: List[Trade] = []

def save_trade(trade: Trade):
    TRADES.append(trade)
    return trade

def get_all_trades():
    return TRADES
