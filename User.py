import db
class User:
    def GetAllPlayers(self):
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
    def GetPlayer(self,name_player):
        data=db.Database().GetAPlayer(name_player)
        print(data)
        return data
    def DeleteUser(self,id_player):
        return db.Database().DeletePlayer(id_player)
