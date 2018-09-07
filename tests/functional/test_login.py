"""
Test login endpoint of API.
"""
import json

def test_login_valid(test_client):
    response = test_client.post(
        '/api/authenticate',
        data=json.dumps({'email': 'test.user@example.net', 'password': 'ValidPassword'}),
        content_type='application/json'
    )
    assert response.status_code == 200
    assert b"auth-token" in response.data

def test_login_invalid(test_client):
    response = test_client.post(
        '/api/authenticate',
        data=json.dumps({'email': 'test.user@example.net', 'password': 'Wrong'}),
        content_type='application/json'
    )
    assert response.status_code == 401
