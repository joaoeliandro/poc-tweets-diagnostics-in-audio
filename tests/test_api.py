from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from ttdiagnosis.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_dashboard_loaded(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK


def test_integrity_format_return_should_be_json(client):
    response = client.get('/')
    assert response.headers['Content-Type'] == 'application/json'
