from repositories import UserRepository

class UserController():
    def __init__(self, repository: UserRepository):
        self._repository = repository
        
    def get_users(self, id: int = None):

        if id == None:
            return self._repository.get_dict_of_users()
        else:
            try:
                return self._repository.get_dict_of_user(id)[0]
            except:
                return ""
    
    def delete_user(self, id: int = None):
        if id == None or id not in self._repository.get_users():
            return False
        else:
            self._repository.delete_user(id)
            return True