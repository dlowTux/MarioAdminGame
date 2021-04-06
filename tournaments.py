import db
class Tournament:
    def GetTournament(self,Type):
        return db.Database().GetTournament(Type)

    def RegisterTournament(self,name,Type):
        return db.Database().RegisterTournament(name,Type)

