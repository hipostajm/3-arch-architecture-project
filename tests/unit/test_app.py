import sys
from flask import Flask

sys.path.append("")

from app.__init__ import __init__

def test_app_is_instance_of_flask():
    assert isinstance(__init__.app, Flask)