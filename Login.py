import db
class Login:
    def __init__(self,user,password):
        self.user=user
        self.password=password
        pass
    def search(self):
        result=db.Database().login(self.user,self.password)
        return result

