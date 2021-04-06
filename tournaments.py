import db
class Tournament:
    def RegisterPointsSeries(self,id_tournament,id_player):
        return db.Database().AddTournamentPointSeries(id_tournament,id_player)

    def GetMemberOfTournamernts(self,id_tournament):
        r=db.Database().GetMemberOfTournamernts(id_tournament)
        if r==None:
            return []
        return r
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

