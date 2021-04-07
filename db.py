import pymysql
class Database:
    
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='usuario',
            password='password',
            db='mariogame'
        )

        self.cursor = self.connection.cursor()
    
    def encript(self,password):
        sql='SELECT HEX(AES_ENCRYPT(%s,%s)) as pass'
        try:
            self.cursor.execute(sql,('has_key',password))
            data = self.cursor.fetchone()
            return  data
        except Exception as e:
            print(e)
            return None
    def GetNamePlayer(self,id_player):
        sql='select name_player from player where id_player=%s'
        try:
            self.cursor.execute(sql,(id_player))
            data=self.cursor.fetchone()
            return data
        except Exception as e:
            print(e)
            return None
    def login(self,user,password):
        sql = 'SELECT id_user FROM user WHERE name_user=%s AND password=%s'
        try:
            d=self.encript(password)
            self.cursor.execute(sql,(user,d[0]))
            data = self.cursor.fetchone()
            return data!=None
        except Exception as e:
            print(e)
            return None

    def GetPlayer(self):
        sql='select * from player order by name_player'
        try:
            self.cursor.execute(sql)
            data=self.cursor.fetchall()
            if data!=None:
                return data
            else:
                return None
        except Exception as e:
            print(e)
            return None
    def GetUUID(self):
        sql='SELECT UUID() AS id'
        try:
            self.cursor.execute(sql)
            data=self.cursor.fetchone()
            return data
        except Exception as e:
            print(e)
            return None
    def InsertPlayer(self, username):
        sql='insert into player values (%s,%s)'
        try:
            d=self.GetUUID()
            self.cursor.execute(sql, (d[0],username))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
    def DeletePlayer(self,id_player):
        sql='DELETE from player where id_player=%s'
        try:
            self.cursor.execute(sql,(id_player))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
    def UpdatePlayer(self,id_player,name_player):
        sql='Update player set name_player=%s where id_player=%s'
        try:
            self.cursor.execute(sql,(name_player,id_player))
            self.connection.commit()
            return True
        except Exception as e:
            print (e)
            return False

    def GetAPlayer(self,name_player):
        sql='select * from player where name_player like %s order by name_player'
        try:
            self.cursor.execute(sql,('%'+name_player+'%'))
            data=self.cursor.fetchall()
            if data!=None:
                return data
            else:
                return None
        except Exception as e:
            print(e)
            return None
    def CheckPlayer(self,id_player):
        sql='select id_player from user_clan where id_player=%s'
        try:
            self.cursor.execute(sql,(id_player))
            data=self.cursor.fetchone()
            if data==None:
                return True
            return False
        except Exception as e:
            print(e)
            return False
    def AddPlayerClan(self,id_player,id_clan):
        sql='insert into user_clan values (%s,%s)'
        try:
            if self.CheckPlayer(id_player):
                self.cursor.execute(sql,(id_clan,id_player))
                self.connection.commit()
                return True
            return False
        except Exception as e:
            print(e)
            return False

    def GetTeams(self):
        sql='select * from clan'
        try:
            self.cursor.execute(sql)
            data=self.cursor.fetchall()
            return data
        except Exception as e:
            print(e)
            return None
    def GetMembersOfClans(self):
        clans=[]
        for x in self.GetTeams():
            clans.append(list(x))
        try:
            count=0
            for clan in clans:
                sql='select p.name_player,p.id_player from user_clan uc inner join player p on p.id_player=uc.id_player where uc.id_clan=%s'
                self.cursor.execute(sql,(clan[0]))
                c=self.cursor.fetchall()
                if c!=None:
                    clans[count].append(c)
                else:
                    clans[count].append([])
                count+=1
            return clans

        except Exception as e:
            print('error ',e)
            return []
    def DeleteAMember(self,id_player):
        sql='delete from user_clan where id_player=%s'
        try:
            self.cursor.execute(sql,(id_player))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def ResetClans(self):
        sql='delete from user_clan'
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False 
    
    def CheckTournament(self,name):
        sql='select * from tournament where tournament_name=%s'
        try:
            self.cursor.execute(sql,(name))
            data=self.cursor.fetchone()
            if data!=None:
                return False
            return True
        except Exception as e:
            print(e)
            return True
    def RegisterTournament(self,name,Type):
        sql='INSERT INTO tournament values (%s,%s,%s)'
        try:
            if self.CheckTournament(name):
                uuid=self.GetUUID()
                self.cursor.execute(sql,(uuid[0],name,Type))
                self.connection.commit()
                return True
            return False
        except Exception as e:
            print('Eror ',e)
            return False
    def GetTournament(self,Type):
        sql='select * from tournament where type_=%s'
        try:
            self.cursor.execute(sql,(Type))
            data=self.cursor.fetchall()
            return data
        except Exception as e:
            print(e)
            return None
    def CheckPlayerTournament(self,id_player):
        sql='select * from  tournament_player where id_player=%s'
        try:
            self.cursor.execute(sql,(id_player))
            data=self.cursor.fetchone()
            if data!=None:
                return False
            return True
        except Exception as e:
            print(e)
            return True
    def AddPlayerTournament(self,id_tournament,id_player):
        sql='insert into  tournament_player values(%s,%s)'
        try:
            if self.CheckPlayerTournament(id_player):
                print('Insert')
                self.cursor.execute(sql,(id_tournament,id_player))
                self.connection.commit()
                return True
            return False
        except Exception as e:
            print(e)
            return False
    def CheckClanTournament(self,id_clan):
        sql='select id_clan from tournament_clans where id_clan =%s'
        try:
            self.cursor.execute(sql,(id_clan))
            a=self.cursor.fetchone()
            if a!=None:
                return False
            return True
        except Exception as e:
            print(e)
            return True
    def AddClanTournament(self,id_tournament,id_clan):
        sql='insert into tournament_clans values(%s,%s)'
        try:
            self.cursor.execute(sql,(id_tournament,id_clan))
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
    def GetMemberOfTournamernts(self,id_tournament):
        sql='select p.name_player from tournament_player tp inner join player p on p.id_player=tp.id_player where tp.id_tournament=%s'
        try:
            self.cursor.execute(sql,(id_tournament))
            data=self.cursor.fetchall()
            return data
        except Exception as e:
            print('Error ',e)
            return None

    def CheckTournamentPoints(self,id_player):
        sql='select *  from tournament_points_series where id_player=%s'
        try:
            self.cursor.execute(sql,(id_player))
            d=self.cursor.fetchone()
            if d!=None:
                return False
            return True
        except Exception as e:
            print(e)
            return True

    def AddTournamentPointSeries(self,id_tournament,id_player):
        sql='insert into tournament_points_series values (%s,%s)'
        try:
            if self.CheckTournamentPoints(id_player):
                self.cursor.execute(sql,(id_tournament,id_player))
                self.connection.commit()
                return True
            return False
        except Exception as e:
            print('Errores ',e)
            return False
    def GetMemberOfPoint(self):
        sql='select p.name_player from tournament_points_series tcs inner join player p on p.id_player=tcs.id_player'
        try:
            self.cursor.execute(sql)
            data=self.cursor.fetchall()
            if data!=None:
                return data
            else:
                return []
        except Exception as e:
            print(e)
            return None


