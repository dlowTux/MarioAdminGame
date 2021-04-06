import db
class Tournament:

    def AddClanTournament(self,id_clan,id_tournament):
        return db.Database().AddClanTournament(id_tournament,id_clan)

    def GetTournament(self,Type):
        data=db.Database().GetTournament(Type)
        if data!=None:
            return data
        return []
    def AddPlayerTournament(self,id_tournament,id_player):
        return db.Database().AddPlayerTournament(id_tournament,id_player)

    def RegisterTournament(self,name,Type):
        return db.Database().RegisterTournament(name,Type)

