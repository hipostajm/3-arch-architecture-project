from flask import Flask, request
from app.controllers import UserController, BadRequest, NotFound
from app.repositories import UserRepository, User

app = Flask(__name__)

custom_responses = {404: (app.redirect("https://http.cat/404"), 404), 200: (app.redirect("https://http.cat/200"), 200), 400: (app.redirect("https://http.cat/400"),400)}

repo = UserRepository()
controller = UserController(repo)

def add_to_repo(user: User):
    repo.users.append(user)
    
def get_from_repo():
    return repo.users

def clear_repo():
    repo.users = []
    repo.free_ids = []

@app.get("/users/")
@app.get("/users/<int:id>")
def get_users(id: int = None):
    try:
        response = controller.get_users(id)
        return response, 200
    except NotFound:
        return custom_responses[404]

@app.delete("/users/<int:id>")
def delete_users(id: int):
    try:
        controller.delete_user(id)
        return custom_responses[200]
    except NotFound:
        return custom_responses[404]

@app.post("/users/")
def post_users():
    try:
        data = request.get_json()
        controller.add_user(data)
        return custom_responses[200]
    except BadRequest:
        return custom_responses[400]

@app.patch("/users/<int:id>")
def patch_users(id: int):
    try:
        data = request.get_json()
        controller.change_user_data(id, data)
        return custom_responses[200]
    except BadRequest:
        return custom_responses[400]

if __name__ == "__main__":
    app.run()