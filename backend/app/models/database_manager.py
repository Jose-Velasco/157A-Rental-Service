import pymysql.cursors

class DatabaseManager:
    host = MYSQL_HOST
    user = MYSQL_USER
    password = MYSQL_PASSWORD
    name = MYSQL_DB
    

    def __init__(self):
        self.connection = connect()

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