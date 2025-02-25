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

    def set_first_name(self, first_name):
        self.first_name = first_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name
    
    def set_birth_year(self, birth_year):
        self.birth_year = birth_year
    
    def set_group(self, group):
        self.group = group
        
    def get_first_name(self) -> str:
        return self.first_name
    
    def get_last_name(self) -> str:
        return self.last_name
    
    def get_birth_year(self) -> int:
        return self.birth_year
    
    def get_group(self) -> str:
        return self.group
        

class UserRepository():
    def __init__(self, group_values: list|tuple[str]):
        self.users: list[User] = [User(1, "Wocjech", "Oczkowski", 2001, "user")] 
        self.free_ids = []
        self.next_id = len(self.users)+1
        self.group_values = group_values
        
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
        
    def append_next_id(self):
        self.next_id += 1
    
    def add_user(self, data: dict):
        self.users.append(User(id = data["id"], first_name=data["firstName"], last_name=data["lastName"],birth_year=data["birthYear"],group=data["group"]))
    
    def change_first_name(self, id, first_name: str):
        for user in self.users:
            if user.id == id:
                user.set_first_name(first_name)
                break
        
    def change_last_name(self,id,last_name: str):
        for user in self.users:
            if user.id == id:
                user.set_last_name(last_name)
                break
        
    def change_birth_year(self,id,birth_year: int):
        for user in self.users:
            if user.id == id:
                user.set_birth_year(birth_year)
                break
                
    def change_group(self,id,group: str):
        for user in self.users:
            if user.id == id:
                user.set_group(group)
                break