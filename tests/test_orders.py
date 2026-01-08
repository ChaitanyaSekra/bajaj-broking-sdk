from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_place_market_order():
    response = client.post(
        "/api/v1/orders",
        json={
            "symbol": "RELIANCE",
            "side": "BUY",
            "orderType": "MARKET",
            "quantity": 10
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "EXECUTED"
    assert "orderId" in data


def test_invalid_quantity():
    response = client.post(
        "/api/v1/orders",
        json={
            "symbol": "RELIANCE",
            "side": "BUY",
            "orderType": "MARKET",
            "quantity": 0
        }
    )
    assert response.status_code == 400
