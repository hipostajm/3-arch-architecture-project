import sys
from flask import Flask
from pytest import fixture

sys.path.append("")

from app.__init__ import __init__

@fixture
def app():
    return __init__.app

def test_app_is_instance_of_flask(app: Flask):
    assert isinstance(app, Flask)