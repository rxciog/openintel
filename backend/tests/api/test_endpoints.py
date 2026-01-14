import pytest
from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app instance

client = TestClient(app)

def test_analyze_ip_endpoint():
    # Test valid IP
    response = client.post("/ip", json={"ip": "8.8.8.8"})
    assert response.status_code == 200
    assert "asn" in response.json()

def test_analyze_ip_invalid_format():
    # Test Pydantic validation for IPvAnyAddress
    response = client.post("/ip", json={"ip": "1234.123.22.1111"})
    assert response.status_code == 422  # Unprocessable Entity

def test_domain_lookup_endpoint():
    # Test valid Domain
    response = client.post("/domain", json={"domain": "google.com"})
    assert response.status_code == 200
    assert response.json()["domain"] == "google.com"

def test_domain_lookup_endpoint_long_str():
    # Test valid Domain
    response = client.post("/domain", json={"domain": "a" * 260})
    assert response.status_code == 422
