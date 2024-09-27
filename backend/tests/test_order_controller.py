from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_get_order():
    response = client.get("/api/v1/order")
    assert response.status_code == 200
    assert "items" in response.json()
    assert "subtotal" in response.json()
    assert "rounds" in response.json()
