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
