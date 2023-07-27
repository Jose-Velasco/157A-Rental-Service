import pymysql.cursors
from pymysql import Connection
from app.configs.api_config import settings

class DatabaseManager:
    host = settings.MYSQL_HOST
    user = settings.MYSQL_USER
    password = settings.MYSQL_PASSWORD
    name = settings.MYSQL_DB
    

    def __init__(self):
        self.connection: Connection = self.connect()

    def connect(self):
        try:
            connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.name,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            return connection
        except Exception as e:
            print(e)
            return None
            raise Exception("Error connecting to database")
    
    def disconnect(self):
        self.connection.close()
    
    def get_connection(self):
        return self.connection