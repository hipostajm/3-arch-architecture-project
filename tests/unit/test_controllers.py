from unittest.mock import Mock, call

from pytest import fixture, raises

from app.repositories import UserRepository
from app.controllers import UserController
from app.__init__ import __init__

@fixture
def repository() -> Mock:
    return Mock(UserRepository)

@fixture
def controller(repository: Mock) -> UserRepository:
    return UserController(repository=repository, custom_responses=__init__.custom_responses)

# def test_calls_repo_on_get_method_with_id(controller: UserController, repository: UserRepository):
    # user_id = 1
    # controller.get_users(user_id)
    # expected = call(id=user_id)
    # assert expected in repository.get_users.mock_calls