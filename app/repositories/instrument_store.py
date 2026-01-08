from app.models.instrument import Instrument

INSTRUMENTS = [
    Instrument(
        symbol="RELIANCE",
        exchange="NSE",
        instrumentType="EQUITY",
        lastTradedPrice=2450
    ),
    Instrument(
        symbol="TCS",
        exchange="NSE",
        instrumentType="EQUITY",
        lastTradedPrice=3890
    ),
    Instrument(
        symbol="INFY",
        exchange="NSE",
        instrumentType="EQUITY",
        lastTradedPrice=1582
    ),
    Instrument(
        symbol="HDFCBANK",
        exchange="NSE",
        instrumentType="EQUITY",
        lastTradedPrice=1675
    ),
    Instrument(
        symbol="ICICIBANK",
        exchange="NSE",
        instrumentType="EQUITY",
        lastTradedPrice=1022
    ),
    Instrument(
        symbol="SBIN",
        exchange="NSE",
        instrumentType="EQUITY",
        lastTradedPrice=642
    ),
    Instrument(
        symbol="ITC",
        exchange="NSE",
        instrumentType="EQUITY",
        lastTradedPrice=456
    ),
    Instrument(
        symbol="BHARTIARTL",
        exchange="NSE",
        instrumentType="EQUITY",
        lastTradedPrice=1188
    ),
    Instrument(
        symbol="LT",
        exchange="NSE",
        instrumentType="EQUITY",
        lastTradedPrice=3520
    ),
    Instrument(
        symbol="AXISBANK",
        exchange="NSE",
        instrumentType="EQUITY",
        lastTradedPrice=1095
    )
]

def get_all_instruments():
    return INSTRUMENTS
