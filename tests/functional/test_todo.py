"""
Testing todo from API.
"""

def test_create_todo(test_client):
    response = test_client.post(
        '/api/todo',
        data={
            'auth-token': 'ValidToken',
            'subject': 'Test todo',
            'description': 'Some sort of todo'
        }
    )
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'id' in json_data
    assert json_data['id'] == 1

def test_list_user_todo(test_client):
    response = test_client.get(
        '/api/todo',
        headers={
            'auth-token': 'ValidToken'
        }
    )
    assert response.status_code == 200
    json_data = json.loads(response.data)

def test_mark_todo_complete(test_client):
    response = test_client.patch(
        '/api/todo/1',
        headers={
            'auth-token': 'ValidToken'
        },
        data=dict(
            status='complete'
        )
    )
    assert response.status_code == 204
    json_data = json.loads(response.data)

def test_delete_todo(test_client):
    response = test_client.delete(
        '/api/todo/1',
        headers={
            'auth-token': 'ValidToken'
        }
    )
    assert response.status_code == 204
    json_data = json.loads(response.data)

