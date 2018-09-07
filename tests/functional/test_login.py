"""
Test login endpoint of API.
"""
def test_login_valid(test_client):
    response = test_client.post(
        '/api/authenticate',
        data=dict(email='test.user@example.net', password='VaildPassword')
    )
    assert response.status_code == 200
    assert b"auth-token" in response.data

def test_login_invalid(test_client):
    response = test_client.post(
        '/api/authenticate',
        data=dict(email='test.user@example.net', password='Wrong')
    )
    assert response.status_code == 403
