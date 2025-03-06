from sys import path

path.append("")

from copy import deepcopy
from pytest import fixture
from app.repositories import UserRepository, User

@fixture
def repository():
    return UserRepository()

def test_repository_get_users(repository: UserRepository):
    expected = User(1, "Woah", "Woah", 2012, "admin")
    repository.users.append(deepcopy(expected))
    assert repository.get_users() == [expected]

def test_repository_get_user(repository: UserRepository):
    user_id = 1
    expected = User(user_id, "Woah", "Woah", 2012, "admin")
    repository.users.append(deepcopy(expected))
    assert repository.get_user(user_id) == expected

def test_repository_delete_user(repository: UserRepository):
    user_id = 1
    user = User(user_id, "Woah", "Woah", 2012, "admin")
    repository.users.append(deepcopy(user))
    repository.delete_user(user_id)
    assert repository.users == []

def test_repository_add_user(repository: UserRepository):
    user = User(1, "Woah", "Woah", 319831, "admin")
    repository.add_user(user.to_dict())
    assert repository.users == [user]

def test_repository_change_first_name(repository: UserRepository):
    user_id = 1
    new_first_name = "Woah"
    user = User(user_id, "123", "456", 481418431, "admin")
    repository.users.append(deepcopy(user))
    repository.change_first_name(user_id, new_first_name)
    user.set_first_name(new_first_name)
    assert [user] == repository.users

def test_repository_change_last_name(repository: UserRepository):
    user_id = 1
    new_last_name = "Woah"
    user = User(user_id, "123", "456", 481418431, "admin")
    repository.users.append(deepcopy(user))
    repository.change_last_name(user_id, new_last_name)
    user.set_last_name(new_last_name)
    assert [user] == repository.users

def test_repository_change_birth_year(repository: UserRepository):
    user_id = 1
    new_birth_year = 9831798173
    user = User(user_id, "123", "456", 481418431, "admin")
    repository.users.append(deepcopy(user))
    repository.change_birth_year(user_id, new_birth_year)
    user.set_birth_year(new_birth_year)
    assert [user] == repository.users

def test_repository_change_group(repository: UserRepository):
    user_id = 1
    new_group = "user"
    user = User(user_id, "123", "456", 481418431, "admin")
    repository.users.append(deepcopy(user))
    repository.change_group(user_id, new_group)
    user.set_group(new_group)
    assert [user] == repository.users
