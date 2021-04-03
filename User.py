import db
class User:
    def GetAllUser(self):
        data=db.Database().GetPlayer()
        if data!=None:
            print(data)
            return data
        else:
            return []

