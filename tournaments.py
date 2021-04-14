import db
class Tournament:
    def GetClashTournament(self,id_tournament):
        return db.Database().GetClashTournament(id_tournament)

    def GetClahsPlayed(self,id_tournament):
        #GetAllTheTeamsOFTournaments
        data=db.Database().GetClansClashTournament(id_tournament)
        points=[]
        for team in data:
            
            aux=[team[0]]
            total=0
            
            result1=db.Database().GetClahsPlayed(id_tournament,team[1],1)
            result2=db.Database().GetClahsPlayed(id_tournament,team[1],2)
            
            aux1=[]
            for r in result1:
                aux1.append(r[0])
                total+=int(r[0])
            
            aux2=[]
            for r in result2:
                aux2.append(r[0])
                total+=int(r[0])

            if len(aux1)>0:
                aux.append(aux1)
            elif len(aux2):
                aux.append(aux2)
            else:
                aux.append([])
            #calculate the sume
            aux.append(total)
            points.append(aux)
        return points


    def Clash(self,id_clan1,id_clan2,id_tournament,ponist1,ponist2):
        r1=self.CheckIfClashExist(id_clan1,id_clan2,id_tournament)
        r2=self.CheckIfClashExist(id_clan2,id_clan1,id_tournament)
        if r1==False and r2==False:
            result=db.Database().RegisterClash(id_clan1,id_clan2,ponist1,ponist2,id_tournament)
            return result
        return False

    def CheckIfClashExist(self,id_clan1,id_clan2,id_tournament):
        return db.Database().CheckIfClashExist(id_clan1,id_clan2,id_tournament)

    

    def GetClansOfTournament(self,id_tournament):
        return db.Database().GetClansOfTournament(id_tournament)

    def StartTournament(self,id_tournament):
        return db.Database().StartTournament(id_tournament)
    
    def DropTeamTournumant(self,id_tournament,id_clan):
        return db.Database().DropTournamentTeam(id_tournament,id_clan)

    def GetStatus(self,id_tournament):
        return db.Database().GetStatus(id_tournament)

    def GetNameTournament(self,id_tournament):
        return db.Database().GetNameTournament(id_tournament)

    def CheckTournamentStatus(self,id_tournament):
        return db.Database().CheckTournamentStatus(id_tournament)
    
    def DeleteTournamentTeam(self,id_tournament):
        return db.Database().DeleteTournamentTeam(id_tournament)

    def DeleteTournamentPlayer(self,id_tournament):
        return db.Database().DeleteTournamentPlayer(id_tournament)

    def GetTournamentPointsSeries(self):
        d=db.Database().GetMemberOfPoint()
        if d==None:
            return []
        else:
            return d

    def RegisterPointsSeries(self,id_tournament,id_player):
        return db.Database().AddTournamentPointSeries(id_tournament,id_player)

    
    def GetMemberOfTournamernts(self,id_tournament):
        r=db.Database().GetMemberOfTournamernts(id_tournament)
        if r==None:
            return []
        else:
            d=[]
            for x in r:
                d.append(x)
            
            return d

    def GetTeamTornament(self,id_tournament):
        r=db.Database().GetTeamTornament(id_tournament)
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

