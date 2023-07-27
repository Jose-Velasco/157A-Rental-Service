from schemas.pydantic.email import Email, EmailCreate, EmailUpdate
from models.database_manager import DatabaseManager

class EmailDao:
    
        def __init__(self):
            self.connection = DatabaseManager().get_connection()
        
        def create_email(self, email: EmailCreate) -> int:
            user_id = email.user_id
            email_address = email.email
    
            try:
                with self.connection.cursor() as cursor:
                    sql = "INSERT INTO `Email` (`user_id`, `email`) VALUES (%s, %s)"
                    self.connection.ping(reconnect=True)
                    cursor.execute(sql, (user_id, email_address))
                    self.connection.commit()
    
                    return cursor.rowcount
            except Exception as e:
                print(e.message)

        def get_email_by_id(self, user_id: int) -> Email:
            try:
                with self.connection.cursor() as cursor:
                    sql = "SELECT * FROM `Email` WHERE `user_id`=%s"
                    self.connection.ping(reconnect=True)
                    cursor.execute(sql, (user_id))
                    result = cursor.fetchall()
    
                    return [Email(**row) for row in result]
            except Exception as e:
                print(e.message)
        
        def update_email(self, email: EmailUpdate) -> int:
            user_id = email.user_id
            email_address = email.email
    
            try:
                with self.connection.cursor() as cursor:
                    sql = "UPDATE `Email` SET `email`=%s WHERE `user_id`=%s"
                    self.connection.ping(reconnect=True)
                    cursor.execute(sql, (user_id, emailmail_address))
                    self.connection.commit()
    
                    return cursor.rowcount
            except Exception as e:
                print(e.message)
        
        def delete_email(self, user_id: int) -> int:
            try:
                with self.connection.cursor() as cursor:
                    sql = "DELETE FROM `Email` WHERE `user_id`=%s"
                    self.connection.ping(reconnect=True)
                    cursor.execute(sql, (user_id))
                    self.connection.commit()
    
                    return cursor.rowcount
            except Exception as e:
                print(e.message)
        
