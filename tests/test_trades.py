from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_trade_created_after_market_order():
    # Step 1: Place a market order
    order_response = client.post(
        "/api/v1/orders",
        json={
            "symbol": "RELIANCE",
            "side": "BUY",
            "orderType": "MARKET",
            "quantity": 3
        }
    )

    assert order_response.status_code == 200
    order_data = order_response.json()
    assert order_data["status"] == "EXECUTED"

    order_id = order_data["orderId"]

    # Step 2: Fetch trades
    trades_response = client.get("/api/v1/trades")
    assert trades_response.status_code == 200

    trades = trades_response.json()
    assert len(trades) > 0

    # Step 3: Validate trade contents
    trade = trades[-1]  # last trade created

    assert trade["orderId"] == order_id
    assert trade["symbol"] == "RELIANCE"
    assert trade["quantity"] == 3
    assert trade["side"] == "BUY"
    assert "tradeId" in trade
    assert "executedAt" in trade
