import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestHealthEndpoint:
    """Tests for the GET /health endpoint."""

    def test_health_returns_200(self):
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_returns_status_ok(self):
        response = client.get("/health")
        assert response.json() == {"status": "ok"}

    def test_health_content_type_is_json(self):
        response = client.get("/health")
        assert "application/json" in response.headers["content-type"]

    def test_health_response_has_no_extra_fields(self):
        response = client.get("/health")
        assert set(response.json().keys()) == {"status"}


class TestEchoEndpoint:
    """Tests for the POST /echo endpoint."""

    def test_echo_returns_200(self):
        response = client.post("/echo", json={"message": "hello"})
        assert response.status_code == 200

    def test_echo_returns_same_message(self):
        response = client.post("/echo", json={"message": "hello"})
        assert response.json() == {"message": "hello"}

    def test_echo_preserves_message_content(self):
        test_messages = [
            "hello world",
            "test message 123",
            "special chars: !@#$%^&*()",
            "unicode: \u00e9\u00e8\u00ea",
            "",
        ]
        for msg in test_messages:
            response = client.post("/echo", json={"message": msg})
            assert response.status_code == 200
            assert response.json() == {"message": msg}

    def test_echo_content_type_is_json(self):
        response = client.post("/echo", json={"message": "hello"})
        assert "application/json" in response.headers["content-type"]

    def test_echo_response_has_no_extra_fields(self):
        response = client.post("/echo", json={"message": "hello"})
        assert set(response.json().keys()) == {"message"}

    def test_echo_missing_message_returns_400(self):
        response = client.post("/echo", json={"foo": "bar"})
        assert response.status_code == 400

    def test_echo_empty_body_returns_400(self):
        response = client.post("/echo", json={})
        assert response.status_code == 400
