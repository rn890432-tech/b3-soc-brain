"""Basic smoke tests for the B3 SOC Brain API."""

from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "b3-soc-brain-api"
    assert data["version"] == "1.0.0"


def test_status():
    response = client.get("/api/v1/status")
    assert response.status_code == 200
    data = response.json()
    assert data["autonomous_ai"] == "running"
    assert data["threat_graph"] == "connected"
    assert data["rule_engine"] == "active"
