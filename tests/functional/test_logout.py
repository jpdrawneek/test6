"""
Testing logging out from API.
"""
import json

def test_valid_token_logout(test_client):
    response = test_client.post(
        '/api/logout/test.user@example.net',
        data=json.dumps({'auth-token': 'ValidToken'}),
        content_type='application/json'
    )
    assert response.status_code == 204
    response = test_client.post(
        '/api/logout/test.user@example.net',
        data=json.dumps({'auth-token': 'ValidToken'}),
        content_type='application/json'
    )
    assert response.status_code == 403

def test_not_valid_token_logout(test_client):
    response = test_client.post(
        '/api/logout/test.user@example.net',
        data=json.dumps({'auth-token': 'NotValidToken'}),
        content_type='application/json'
    )
    assert response.status_code == 403
