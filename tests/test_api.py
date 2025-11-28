import os
import sys
import pytest

# Ensure project root is in the Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
    
from app import create_app

@pytest.fixture
def flask_app():
    """Create a Flask app instance configured for testing."""
    app = create_app()
    app.config.update(TESTING=True)
    return app


@pytest.fixture
def client(flask_app):
    return flask_app.test_client()


def test_get_regions_returns_list(client):
    """GET /api/regions should return a list of regions."""
    resp = client.get("/api/regions")
    assert resp.status_code == 200

    data = resp.get_json()
    assert isinstance(data, list)
    if data:
        assert "id" in data[0]
        assert "name" in data[0]


def test_get_players_returns_list(client):
    """GET /api/players should return a list of players."""
    resp = client.get("/api/players")
    assert resp.status_code == 200

    data = resp.get_json()
    assert isinstance(data, list)


def test_create_player_success(client):
    """POST /api/players should create a new player."""
    new_player = {"username": "pytest-hero"}

    resp = client.post("/api/players", json=new_player)
    assert resp.status_code == 201

    created = resp.get_json()
    assert created["username"] == "pytest-hero"
    assert created["level"] == 1
    assert created["xp"] == 0
    assert "id" in created

    # Verify player now exists in list
    resp_list = client.get("/api/players")
    assert resp_list.status_code == 200
    players = resp_list.get_json()

    assert any(p["id"] == created["id"] for p in players)
