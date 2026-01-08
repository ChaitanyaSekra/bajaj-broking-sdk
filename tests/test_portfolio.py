from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_portfolio_after_trade():
    # Place a market buy order
    client.post(
        "/api/v1/orders",
        json={
            "symbol": "RELIANCE",
            "side": "BUY",
            "orderType": "MARKET",
            "quantity": 2
        }
    )

    # Fetch portfolio
    response = client.get("/api/v1/portfolio")
    assert response.status_code == 200

    portfolio = response.json()
    assert len(portfolio) > 0

    item = portfolio[0]
    assert item["symbol"] == "RELIANCE"
    assert item["quantity"] >= 2
    assert "averagePrice" in item
    assert "currentValue" in item
