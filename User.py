import db
class User:
    def GetAllUser(self):
        data=db.Database().GetPlayer()
        if data!=None:
            return data
        else:
            return []
    def RegisterUser(self,username):
        if db.Database().InsertPlayer(username):
            print('True')
            return True
        else:
            print(False)
            return False

