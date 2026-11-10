from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check_returns_status():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "funcionando"} 

def test_saude_check_returns_status():
    response = client.get("/saude")

    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}