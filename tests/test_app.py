from app.app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["application"] == "ShopEasy"
    assert data["version"] == "1.0"
    assert data["status"] == "running"

def test_products():
    client = app.test_client()
    response = client.get("/products")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 3
    assert data[0]["name"] == "Laptop"

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"
