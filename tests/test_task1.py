"""First Test to make sure it runs locally"""
from flask_jwt_extended import create_access_token, decode_token

from app import User


def test_register(client):
    """This registers the user"""
    data = {"attributes": {"username": "keith", "password": "test"}, "type": "User"}
    response = client.post("/register", json={"data": data})
    response_data = response.get_json()
    assert response.status_code == 201
    assert response_data == "Created User"


def test_auth(client, create_user):
    """Test User Authentication"""
    data = {"attributes": {"username": "testUser", "password": "test"}, "type": "User"}
    response = client.post("/auth", json={"data": data})
    response_data = response.get_json()
    access_token = response_data['access_token']
    token_value = decode_token(access_token)
    assert token_value['sub'] == 'testUser'


def test_protected(client, create_user):
    with client.application.app_context():
        access_token = create_token()
    token_value = decode_token(access_token)
    username = token_value['sub']
    assert username == 'testUser'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    response = client.get('/user_info', headers=headers)
    response_data = response.get_json()
    assert response_data['username'] == 'testUser'


def create_token():
    user = User.query.first()
    access_token = create_access_token(user.username)
    return access_token
