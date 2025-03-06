from app.repositories import UserRepository

class NotFound(Exception):
    pass

class BadRequest(Exception):
    pass

class UserController():
    def __init__(self, repository: UserRepository, ):
        self._repository = repository
        
    def get_users(self, id: int = None) -> list[dict]|dict:

        users = self._repository.get_users()

        if id == None:
            return [user.to_dict() for user in users]
        
        elif id in users:
            return self._repository.get_user(id).to_dict()
        
        else:
            raise NotFound
    
    def delete_user(self, id: int = None) -> None:
        if id == None or id not in self._repository.get_users():
            raise NotFound 
        else:
            self._repository.delete_user(id)
    
    def add_user(self, user_data: dict) -> None:
        if {"firstName", "lastName", "birthYear", "group"} == set(user_data.keys()) and user_data["group"] in ["user", "premium", "admin"] and type(user_data["birthYear"]) == int and type(user_data["firstName"]) == str and type(user_data["lastName"]) == str:
           
            id = 0
            
            if self._repository.free_ids:
                id = self._repository.free_ids[0]
            else:
                id = self._repository.next_id
                self._repository.append_next_id()
            
            user_data["id"] = id
            self._repository.add_user(user_data)
        
        else:
            raise BadRequest
        
    def change_user_data(self,id: int ,user_data: dict) -> None:
        
        keys = user_data.keys() 
        
        changes = dict()
        
        for key in keys:
            if key not in ["firstName", "lastName", "birthYear", "group"]:
                raise BadRequest
        
        if id not in self._repository.get_users():
            raise BadRequest
        
        if (data := "firstName") in keys:
            if type(user_data[data]) == str:
                changes[self._repository.change_first_name] = user_data[data] 
            else:
                raise BadRequest
        
        if (data := "lastName") in keys:
            if type(user_data[data]) == str:
                changes[self._repository.change_last_name] = user_data[data]
            else:
                raise BadRequest
        
        if (data := "birthYear") in keys:
            if type(user_data[data]) == int:                
                changes[self._repository.change_birth_year] = user_data[data]
            
            else:
                raise BadRequest
        
        if (data := "group") in keys:
            if user_data[data] in ['user', "admin", "premium"]:
                changes[self._repository.change_group] = user_data[data]
            else:
                raise BadRequest
        
        if changes:
            for changer, arg in changes.items():
                changer(id, arg)
        else:
            raise BadRequest