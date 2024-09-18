from fastapi.testclient import TestClient

from books.api import v0

def test_index():
    client = TestClient(v0.app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Book API v0"}
