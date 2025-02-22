class User():
    def __init__(self, id: int, name: str, lastname:str, birth_year: int, group: str):
        self.id = id
        self.name = name
        self.lastname = lastname
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
        return {"id": self.id, "firstName": self.name, "lastName": self.lastname, "birthYear": self.birth_year, "group": self.group}
        

class UserRepository():
    def __init__(self):
        self.users: list[User] = [User(1, "Wocjech", "Oczkowski", 2001, "user")] 
        
    def get_users(self):
        return self.users
    
    def get_dict_of_users(self):
        return [user.to_dict() for user in self.users]
        
    def get_user(self, id):
        return [user for user in self.users if user.id == id]
    
    def get_dict_of_user(self, id):
        return [user.to_dict() for user in self.users if user.id == id]
    
    def delete_user(self, id):
        for i, user in enumerate(self.users):
            if id == user.id:
                del self.users[i]