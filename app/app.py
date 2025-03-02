from flask import Flask, request
from app.controllers import UserController
from app.repositories import UserRepository, User

app = Flask(__name__)

custom_responses = {404: app.redirect("https://http.cat/404"), 200: app.redirect("https://http.cat/200"), 400: app.redirect("https://http.cat/400")}

repo = UserRepository(group_values=["user", "premium", "admin"])
controller = UserController(repo, custom_responses=custom_responses)

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
    response = controller.get_users(id) 
    return response

@app.delete("/users/<int:id>")
def delete_users(id: int):
    response = controller.delete_user(id)
    return response

@app.post("/users/")
def post_users():
    data = request.get_json()
    response = controller.add_user(data)
    return response

@app.patch("/users/<int:id>")
def patch_users(id: int):
    data = request.get_json()
    response = controller.change_user_data(id, data)
    return response

if __name__ == "__main__":
    app.run()