from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_start():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "biker02"}
