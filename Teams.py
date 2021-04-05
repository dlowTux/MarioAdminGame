import db
class Team:
    def GetTeams(self):
        return db.Database().GetMembersOfClans()
    def AddPlayerClan(self,id_clan,id_player):
        return db.Database().AddPlayerClan(id_player,id_clan)
    

