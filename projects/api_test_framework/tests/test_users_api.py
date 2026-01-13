import requests
import pytest

def test_get_users_status_code(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200

def test_get_users_response_is_json(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.headers["Content-Type"].startswith("application/json")

def test_get_users_response_structure(base_url):
    response = requests.get(f"{base_url}/users")
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    user = data[0]
    assert "id" in user
    assert "name" in user
    assert "email" in user

@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_get_user_by_id(base_url, user_id):
    response = requests.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, dict)

    assert data["id"] == user_id
    is_empty_name = "name" in data
    is_empty_email = "email" in data
    assert is_empty_name
    assert is_empty_email
    if not is_empty_name: assert len(data["name"]) > 0
    if not is_empty_email: assert len(data["email"]) > 0 

@pytest.mark.parametrize("user_id", [-1, 0, 9999999])
def test_get_invalid_user_id(base_url, user_id):
    response = requests.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 404

@pytest.mark.parametrize("data_type", ["invdata", "abc", "123", "@!#"])
def test_get_invalid_data_type(base_url, data_type):
    response = requests.get(f"{base_url}/data_type")
    assert response.status_code == 404
