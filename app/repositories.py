class User():
    def __init__(self, id: int, first_name: str, last_name:str, birth_year: int, group: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.group = group
    
    def __eq__(self, value) -> bool:
        if isinstance(value, User):
            return self.id == value.id
        elif isinstance(value, int|float):
            return self.id == value 
        else:
            raise NotImplementedError
    
    def __repr__(self) -> str:
        return str(self.id)
    
    def to_dict(self) -> dict:
        return {"id": self.id, "firstName": self.first_name, "lastName": self.last_name, "birthYear": self.birth_year, "group": self.group}
        

class UserRepository():
    def __init__(self):
        self.users: list[User] = [User(1, "Wocjech", "Oczkowski", 2001, "user")] 
        self.free_ids = []
        self.next_id = len(self.users)+1
        
    def get_users(self):
        return self.users

    def get_user(self, id):
        return [user for user in self.users if user.id == id][0]
    
    def delete_user(self, id):
        for i, user in enumerate(self.users):
            if id == user.id:
                self.free_ids.append(id)
                del self.users[i]
                break
    
    def add_user(self, data: dict):
        self.users.append(User(id = data["id"], first_name=data["firstName"], last_name=data["lastName"],birth_year=data["birthYear"],group=data["group"]))