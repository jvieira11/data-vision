from fastapi.testclient import TestClient  # noqa: I001
from app.main import app


client = TestClient(app)


def test_health_check_returns_status():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "funcionando"}


def test_unknown_route_returns_404():
    response = client.get("/saude")

    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_health_version_check():
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {"version": "0.1.0"}
