from app.models.database_manager import DatabaseManager
from app.schemas.pydantic.returned import Return

class ReturnedDAO:

    def __init__(self):
        self.connection = DatabaseManager().get_connection()
    
    def set_returned(self, returned: Return):
        try:
            with self.connection.cursor() as cursor:
                sql = """
                        INSERT INTO Returned (transaction_id, title)
                        VALUES (%s, %s)
                        """
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (returned.transaction_id, returned.title))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
            raise Exception("Error on create returned")
    
    def get_all_returned(self, user_id: int):
        try:
            with self.connection.cursor() as cursor:
                sql = """
                        SELECT * FROM Returned
                        WHERE transaction_id IN (
                            SELECT transaction_id FROM Transaction
                            WHERE user_id = %s
                        )
                        """
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id))
                results = cursor.fetchall()
                output = {}
                for result in results:
                    if f"{result['transaction_id']}{result['title']}" not in output:
                        output[f"{result['transaction_id']} {result['title']}"] = True
                return output

        except Exception as e:
            print(e)
            raise Exception("Error on get all returned")