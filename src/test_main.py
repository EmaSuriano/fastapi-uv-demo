from fastapi.testclient import TestClient
from main import app

# Create a test client
client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}


def test_create_item():
    test_item = {"name": "Test Item", "price": 10.5, "is_offer": True}
    response = client.post("/items/", json=test_item)
    assert response.status_code == 200
    assert response.json() == test_item
