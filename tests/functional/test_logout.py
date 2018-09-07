"""
Testing logging out from API.
"""

def test_valid_token_logout(test_client):
    response = test_client.post(
        '/api/logout',
        data={'auth-token': 'ValidToken'}
    )
    assert response.status_code == 204
    response = test_client.post(
        '/api/logout',
        data={'auth-token': 'ValidToken'}
    )
    assert response.status_code == 401

def test_not_valid_token_logout(test_client):
    response = test_client.post(
        '/api/logout',
        data={'auth-token': 'NotValidToken'}
    )
    assert response.status_code == 401
