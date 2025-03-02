from http import HTTPStatus
from flask.testing import FlaskClient
from pytest import fixture
from sys import path

path.append("")

from app.__init__ import __init__
from app.controllers import UserController
from app.repositories import UserRepository, User

@fixture
def client() -> FlaskClient:
    return __init__.app.test_client()

def test_get_users_with_out_id_returns_status_200(client: FlaskClient):
    response = client.get(f"/users/")
    assert response.status_code == HTTPStatus.OK

def test_get_users_with_out_id_and_values_returns_correct_values(client: FlaskClient):
    __init__.clear_repo()
    response = client.get(f"/users/")
    assert response.json == []
    __init__.clear_repo()
    
def test_get_users_with_out_id_and_with_multiple_values_returns_correct_values(client: FlaskClient):
    __init__.clear_repo()
    expected = [User(1, "Imie", "Nazwikso", 2002, "user"), User(2, "Woah", "Kowalska", 9212, "admin")]
    __init__.add_to_repo(expected[0])
    __init__.add_to_repo(expected[1])
    response = client.get(f"/users/")
    assert response.json == [user.to_dict() for user in expected]
    __init__.clear_repo()
    
def test_get_user_with_id_and_returns_status_200(client: FlaskClient):
    __init__.clear_repo()
    id = 1
    expected = User(id, "K", "P", 2009, "user")
    __init__.add_to_repo(expected)
    response = client.get(f"/users/{id}")
    assert response.json == expected.to_dict() and response.status_code == HTTPStatus.OK
    __init__.clear_repo()
    
def test_get_out_of_range_user(client: FlaskClient):
    __init__.clear_repo()
    id = 2
    expected = HTTPStatus.NOT_FOUND
    response = client.get(f"/users/{id}")
    assert response.status_code == expected
    __init__.clear_repo()

def test_delete_with_valid_data(client: FlaskClient):
    __init__.clear_repo()
    id = 1
    excepted = HTTPStatus.OK
    __init__.add_to_repo(User(id, "I", "N", 2008, "user"))
    response = client.delete(f"/users/{id}")
    assert response.status_code == excepted
    __init__.clear_repo()

def test_delete_with_out_of_range_index(client: FlaskClient):
    __init__.clear_repo()
    id = 1
    excepted = HTTPStatus.NOT_FOUND
    response = client.delete(f"/users/{id}")
    assert response.status_code == excepted
    __init__.clear_repo()

def test_post_user_with_valid_data(client: FlaskClient):
    __init__.clear_repo()
    id = 1
    excepted = {"firstName": "imie", "lastName": "WoaH", "birthYear": 2012, "group": 'user'}
    client.post("/users/", json=excepted)
    excepted["id"] = id
    assert excepted == client.get(f"/users/{id}").json
    __init__.clear_repo()

def test_post_user_with_unvalid_data(client: FlaskClient):
    __init__.clear_repo()
    excepted = HTTPStatus.BAD_REQUEST
    response = client.post("/users/", json={"woah": "woah"})
    assert response.status_code == excepted
    __init__.clear_repo()
    
def test_post_user_with_unvalid_group(client: FlaskClient):
    __init__.clear_repo()
    excepted = HTTPStatus.BAD_REQUEST
    response = client.post("/users/", json={"firstName": "imie", "lastName": "WoaH", "birthYear": 2012, "group": 'rovrbvoirjbvirbvou'})
    assert response.status_code == excepted
    __init__.clear_repo()
    
    
def test_patch_user_with_valid_data(client: FlaskClient):
    __init__.clear_repo()
    id = 1
    name = "Woah"
    __init__.add_to_repo(User(id, "darek", "warek", 387812, "user"))
    response = client.patch(f"/users/{id}", json={"firstName": name})
    assert response.status_code == HTTPStatus.OK
    assert client.get(f"/users/{id}").json["firstName"] == name
    __init__.clear_repo()

def test_patch_with_unvalid_data(client: FlaskClient):
    __init__.clear_repo()
    id = 1
    __init__.add_to_repo(User(id, "woah", "wwa", 3712, "admin"))
    response = client.patch(f"/users/{id}", json={'ude': 102})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    __init__.clear_repo()

def test_patch_with_out_of_range_group(client: FlaskClient):
    __init__.clear_repo()
    id = 1
    __init__.add_to_repo(User(id, "woah", 'haoW', 1723213, "user"))
    response = client.patch(f"/users/{id}", json={'group': "Woahaaa"})
    assert response.status_code == HTTPStatus.BAD_REQUEST
    __init__.clear_repo()
    
def test_patch_with_multiple_valid_data(client: FlaskClient):
    __init__.clear_repo()
    id = 1
    expected = {"firstName": "wdu9uwhdw", "lastName": "WoaHaoW", "birthYear": 2481, "group":"premium"}
    __init__.add_to_repo(User(id, "dijefdjecwin", "cneeoucnon", 38137813813, "user"))
    client.patch(f"/users/{id}", json=expected)
    expected["id"] = id
    assert expected == client.get(f"/users/{id}").json