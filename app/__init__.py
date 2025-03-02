from dataclasses import dataclass
from types import FunctionType
from flask import Flask

from app.app import get_users, post_users, patch_users, delete_users, app, custom_responses, add_to_repo, clear_repo, get_from_repo

@dataclass
class views:
    app: Flask
    get_users: FunctionType
    post_users: FunctionType
    patch_users: FunctionType
    delete_users: FunctionType
    custom_responses: dict
    add_to_repo: FunctionType
    clear_repo: FunctionType
    get_from_repo: FunctionType
    
__init__ = views(app=app, get_users=get_users, post_users=post_users, patch_users=patch_users, delete_users=delete_users, custom_responses=custom_responses, add_to_repo=add_to_repo, clear_repo=clear_repo, get_from_repo=get_from_repo)

