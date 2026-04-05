"""
TODO: Write tests for the FreshEye API.

Test ideas:
1. Health check returns 200
2. Classify endpoint accepts an image
3. Classify endpoint rejects non-image files
4. Response has required fields (item, freshness, confidence, tips)
"""

import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_health_check():
    """Test that the health endpoint returns OK."""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_home_page():
    """Test that the home page loads."""
    response = client.get("/")
    assert response.status_code == 200
    assert "FreshEye" in response.text


# TODO: Add more tests!
# def test_classify_image():
#     ...
