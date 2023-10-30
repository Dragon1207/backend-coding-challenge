import json
import pytest

from gistapi import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_ping(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "pong"


def test_search_no_matches(client):
    payload = {"username": "justdionysus", "pattern": "foobar"}
    response = client.post("/api/v1/search", json=payload)
    assert response.status_code == 200
    data = json.loads(response.data.decode("utf-8"))
    assert data["status"] == "success"
    assert data["username"] == "justdionysus"
    assert data["pattern"] == "foobar"
    assert data["matches"] == []


def test_search_with_matches(client):
    payload = {"username": "justdionysus", "pattern": "import requests"}
    response = client.post("/api/v1/search", json=payload)
    assert response.status_code == 200
    data = json.loads(response.data.decode("utf-8"))
    assert data["status"] == "success"
    assert data["username"] == "justdionysus"
    assert data["pattern"] == "import requests"
    assert len(data["matches"]) > 0


if __name__ == "__main__":
    pytest.main()
