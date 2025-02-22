from repositories import UserRepository

class UserController():
    def __init__(self, repository: UserRepository, custom_responses: dict):
        self._repository = repository
        self.custom_responses = custom_responses
        
    def get_users(self, id: int = None):

        if id == None:
            status_code = 200
            return [user.to_dict() for user in self._repository.get_users()], status_code
        
        elif id in self._repository.get_users():
            status_code = 200
            return self._repository.get_user(id).to_dict(), status_code
        
        else:
            status_code = 404
            return self.custom_responses[status_code], status_code
    
    def delete_user(self, id: int = None):
        if id == None or id not in self._repository.get_users():
            status_code = 404
            return self.custom_responses[status_code], status_code 
        
        else:
            self._repository.delete_user(id)
            status_code = 200
            return self.custom_responses[status_code], status_code
    
    def add_user(self, user_data: dict):
        users = self._repository.get_users()
        
        if "firstName" in user_data.keys() and "lastName" in user_data.keys() and "birthYear" in user_data.keys() and "group" in user_data.keys() and user_data["group"] in ["user", "premium", "admin"] and type(user_data["birthYear"]) == int and type(user_data["firstName"]) == str and type(user_data["lastName"]) == str:
            status_code = 200
            
            id = 0
            
            if self._repository.free_ids:
                id = self._repository.free_ids[0]
            else:
                id = self._repository.next_id
                self._repository.next_id += 1
            
            user_data["id"] = id
            
            self._repository.add_user(user_data)
            return self.custom_responses[status_code], status_code
        else:
            status_code = 400
            return self.custom_responses[status_code], status_code
            