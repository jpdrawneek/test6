from src.model import Todo

def test_merge_updates():
    item = Todo(id=1, user_id=1, summary='test update', status='New')
    test_data = {
        'status': 'complete'
    }
    result = item.merge_update(test_data)
    assert result is True
    assert item.status == 'complete'
    assert item.id == 1
    assert item.summary == 'test update'
    assert item.description is None
    assert item.user_id == 1

def test_merge_updates_invalid_data():
    item = Todo(id=1, user_id=1, summary='test update', status='New')
    test_data = {
        'status': 'complete',
        'stuff': 'foobar'
    }
    result = item.merge_update(test_data)
    assert result is False
    assert item.status == 'complete'
    assert item.id == 1
    assert item.summary == 'test update'
    assert item.description is None
    assert item.user_id == 1
    assert hasattr(item, 'stuff') is False

def test_merge_updates_cant_change_user():
    item = Todo(id=1, user_id=1, summary='test update', status='New')
    test_data = {
        'status': 'complete',
        'user_id': 2
    }
    result = item.merge_update(test_data)
    assert result is False
    assert item.status == 'complete'
    assert item.id == 1
    assert item.summary == 'test update'
    assert item.description is None
    assert item.user_id == 1

def test_merge_updates_cant_change_id():
    item = Todo(id=1, user_id=1, summary='test update', status='New')
    test_data = {
        'status': 'complete',
        'id': 2
    }
    result = item.merge_update(test_data)
    assert result is False
    assert item.status == 'complete'
    assert item.id == 1
    assert item.summary == 'test update'
    assert item.description is None
    assert item.user_id == 1
