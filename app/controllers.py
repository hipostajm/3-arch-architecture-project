from app.repositories import UserRepository
from flask import Response

class UserController():
    def __init__(self, repository: UserRepository, custom_responses: dict):
        self._repository = repository
        self.custom_responses = custom_responses
        
    def get_users(self, id: int = None) -> tuple[Response, int]:

        if id == None:
            status_code = 200
            return [user.to_dict() for user in self._repository.get_users()], status_code
        
        elif id in self._repository.get_users():
            status_code = 200
            return self._repository.get_user(id).to_dict(), status_code
        
        else:
            status_code = 404
            return self.custom_responses[status_code], status_code
    
    def delete_user(self, id: int = None) -> tuple[Response, int]:
        if id == None or id not in self._repository.get_users():
            status_code = 404
            return self.custom_responses[status_code], status_code 
        
        else:
            self._repository.delete_user(id)
            status_code = 200
            return self.custom_responses[status_code], status_code
    
    def add_user(self, user_data: dict) -> tuple[Response, int]:
        if {"firstName", "lastName", "birthYear", "group"} == set(user_data.keys()) and user_data["group"] in self._repository.group_values and type(user_data["birthYear"]) == int and type(user_data["firstName"]) == str and type(user_data["lastName"]) == str:
            
            status_code = 200
           
            id = 0
            
            if self._repository.free_ids:
                id = self._repository.free_ids[0]
            else:
                id = self._repository.next_id
                self._repository.append_next_id()
            
            user_data["id"] = id
            
            self._repository.add_user(user_data)
            return self.custom_responses[status_code], status_code
        
        else:
            status_code = 400
            return self.custom_responses[status_code], status_code
        
    def change_user_data(self,id: int ,user_data: dict) -> tuple[Response, int]:
        
        keys = user_data.keys() 
        
        changes = dict()
        
        for key in keys:
            if key not in ["firstName", "lastName", "birthYear", "group"]:
                status_code = 400
                return self.custom_responses[status_code], status_code
        
        if id not in self._repository.get_users():
            status_code = 400
            return self.custom_responses[status_code], status_code
        
        if (data := "firstName") in keys:
            if type(user_data[data]) == str:
                changes[self._repository.change_first_name] = user_data[data] 
            else:
                status_code = 400
                return self.custom_responses[status_code], status_code
        
        if (data := "lastName") in keys:
            if type(user_data[data]) == str:
                changes[self._repository.change_last_name] = user_data[data]
            else:
                status_code = 400
                return self.custom_responses[status_code], status_code
        
        if (data := "birthYear") in keys:
            if type(user_data[data]) == int:                
                changes[self._repository.change_birth_year] = user_data[data]
            
            else:
                status_code = 400
                return self.custom_responses[status_code], status_code 
        
        if (data := "group") in keys:
            if user_data[data] in self._repository.group_values:
                changes[self._repository.change_group] = user_data[data]
            
            else:
                status_code = 400
                return self.custom_responses[status_code], status_code
        
        if changes:
            for changer, arg in changes.items():
                changer(id, arg)
            status_code = 200
            return self.custom_responses[status_code], status_code
        else:
            status_code = 400
            return self.custom_responses[status_code], status_code