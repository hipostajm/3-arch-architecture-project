from unittest.mock import MagicMock, call

from pytest import fixture, raises

from app.repositories import UserRepository
from app.controllers import UserController, BadRequest, NotFound
from app.__init__ import __init__

@fixture
def repository() -> MagicMock:
    return MagicMock(UserRepository)

@fixture
def controller(repository: MagicMock) -> UserController:
    return UserController(repository=repository)

def test_controller_calls_repo_on_get_method_with_id(controller: UserController, repository: MagicMock):
    user_id = 1
    repository.get_users.return_value.__contains__.side_effect = lambda x: x == user_id
    controller.get_users(user_id)
    expected = call(user_id)
    assert expected in repository.get_user.mock_calls

def test_controller_calls_repo_on_get_method_with_out_id(controller: UserController, repository: MagicMock):
    controller.get_users()
    expected = call()
    assert expected in repository.get_users.mock_calls

def test_controller_calls_repo_and_rises_a_not_found_exception_with_unvalid_id(controller: UserController, repository: MagicMock):
    user_id = 1
    repository.get_users.return_value.__contains__.side_effect = lambda x: x != user_id
    with raises(NotFound):
        controller.get_users(user_id)
        assert repository.get_user_mock_calls == []

def test_controller_dont_calls_repo_on_delete_with_unvalid_id(controller: UserController, repository: MagicMock):
    user_id = 1
    repository.get_users.return_value.__contains__.side_effect = lambda x: x != user_id
    with raises(NotFound):
        controller.delete_user(user_id)
        assert repository.delete_user.mock_calls == []

def test_controller_calls_repo_on_delete_with_valid_id(controller: UserController, repository: MagicMock):
    user_id = 1
    repository.get_users.return_value.__contains__.side_effect = lambda x: x == user_id
    controller.delete_user(user_id)
    expected = call(user_id)
    assert expected in repository.delete_user.mock_calls

def test_controller_calls_repo_on_add_user_with_valid_data(controller: UserController, repository: MagicMock):
    data = {"firstName": "Woah", "lastName": "Woah", "birthYear": 2002, "group": "user"}
    user_id = 1
    repository.free_ids = []
    repository.next_id = user_id
    controller.add_user(data)
    data["id"] == user_id
    expected = call(data)
    assert expected in repository.add_user.mock_calls

def test_controller_raises_and_call_on_add_user_with_unvalid_data(controller: UserController, repository: MagicMock):
    data = {}
    with raises(BadRequest):
        controller.add_user(data)
        assert not repository.add_user.mock_calls

def test_controller_call_repo_change_first_name_method_on_change_user_with_valid_data(controller: UserController, repository: MagicMock):
    data_value = "Woah"
    data = {"firstName": data_value}
    user_id = 1
    repository.get_users.return_value.__contains__.side_effect = lambda x: x == user_id
    controller.change_user_data(user_id, data)
    expetcted = call(user_id, data_value)
    assert expetcted in repository.change_first_name.mock_calls


def test_controller_call_repo_change_last_name_method_on_change_user_with_valid_data(controller: UserController, repository: MagicMock):
    data_value = "Woah"
    data = {"lastName": data_value}
    user_id = 1
    repository.get_users.return_value.__contains__.side_effect = lambda x: x == user_id
    controller.change_user_data(user_id, data)
    expetcted = call(user_id, data_value)
    assert expetcted in repository.change_last_name.mock_calls


def test_controller_call_repo_change_birth_year_name_method_on_change_user_with_valid_data(controller: UserController, repository: MagicMock):
    data_value = 2091
    data = {"birthYear": data_value}
    user_id = 1
    repository.get_users.return_value.__contains__.side_effect = lambda x: x == user_id
    controller.change_user_data(user_id, data)
    expetcted = call(user_id, data_value)
    assert expetcted in repository.change_birth_year.mock_calls


def test_controller_call_repo_change_group_method_on_change_user_with_valid_data(controller: UserController, repository: MagicMock):
    data_value = "admin"
    data = {"group": data_value}
    user_id = 1
    repository.get_users.return_value.__contains__.side_effect = lambda x: x == user_id
    controller.change_user_data(user_id, data)
    expetcted = call(user_id, data_value)
    assert expetcted in repository.change_group.mock_calls

def test_controller_dont_call_repo_and_raises_on_change_user_with_unvalid_data(controller: UserController, repository: MagicMock):
    user_id = 1
    repository.get_users.return_value.__contains__.side_effect = lambda x: x != user_id
    with raises(BadRequest):
        controller.change_user_data(user_id, {"woah": "woah"})
        assert not repository.change_group.mock_calls and not repository.change_birth_year.mock_calls and not repository.change_last_name.mock_calls and not repository.change_first_name.mock_calls