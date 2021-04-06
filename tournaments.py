import db
class Tournament:
    def GetTournament(self,Type):
        data=db.Database().GetTournament(Type)
        if data!=None:
            return data
        return []
    def AddPlayerTournament(self,id_tournament,id_player):
        return db.Database().AddPlayerTournament(id_tournament,id_player)

    def RegisterTournament(self,name,Type):
        return db.Database().RegisterTournament(name,Type)

