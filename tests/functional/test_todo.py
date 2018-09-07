"""
Testing todo from API.
"""
import json

def test_create_todo(test_client):
    response = test_client.post(
        '/api/todo',
        json={
            'summary': 'Test todo',
            'description': 'Some sort of todo'
        },
        headers={
            'auth-token': 'ValidToken'
        }
    )
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'id' in json_data
    assert json_data['id'] == 2

def test_list_user_todo(test_client):
    response = test_client.get(
        '/api/todo',
        headers={
            'auth-token': 'ValidToken'
        }
    )
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) == 1
    item = json_data.pop()
    assert 'id' in item
    assert 'summary' in item
    assert item['summary'] == 'test1'

def test_mark_todo_complete(test_client):
    response = test_client.patch(
        '/api/todo/1',
        headers={
            'auth-token': 'ValidToken'
        },
        json={
            'status': 'complete'
        }
    )
    assert response.status_code == 204
    json_data = response.get_json()
    assert json_data is None
    response = test_client.get(
        '/api/todo/1',
        headers={
            'auth-token': 'ValidToken'
        }
    )
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['id'] == 1
    assert json_data['status'] == 'complete'

def test_delete_todo(test_client):
    response = test_client.delete(
        '/api/todo/1',
        headers={
            'auth-token': 'ValidToken'
        }
    )
    assert response.status_code == 204
    json_data = response.get_json()
    assert json_data is None
    response = test_client.get(
        '/api/todo/1',
        headers={
            'auth-token': 'ValidToken'
        }
    )
    assert response.status_code == 404
