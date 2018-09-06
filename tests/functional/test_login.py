"""
Test login endpoint of API.
"""
def test_login_valid(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
