import db
class Team:
    def GetTeams(self):
        data=db.Database().GetMembersOfClans()
        if data!=None:
            return data
        return []
    def AddPlayerClan(self,id_clan,id_player):
        return db.Database().AddPlayerClan(id_player,id_clan)
    def DeleteMemberClan(self,id_player):
        return db.Database().DeleteAMember(id_player)
    def ResetClans(self):
        return db.Database().ResetClans()
