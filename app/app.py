from flask import Flask, request
from controllers import UserController
from repositories import UserRepository

app = Flask(__name__)

controller = UserController(UserRepository())

errors = {404: app.redirect("https://http.cat/404")}

@app.get("/users/")
@app.get("/users/<int:id>")
def get_users(id: int = None):
    response = controller.get_users(id) 
    if response:
        return response, 200
    else:
        return errors[404], 404

@app.delete("/users/<int:id>")
def delete_user(id: int):
    if controller.delete_user(id):
        return "",200
    else:
        return errors[404], 404

@app.post("/users/")
def post_user():
    data = request.get_json()
    print(type(data), data)
    return "", 200

if __name__ == "__main__":
    app.run()