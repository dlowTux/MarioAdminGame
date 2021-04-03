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
        sql='select * from player'
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
