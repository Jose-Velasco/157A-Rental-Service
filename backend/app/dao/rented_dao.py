from app.schemas.pydantic.rented import CreateRented, UpdateRented, Rented
from app.models.database_manager import DatabaseManager
from typing import List

class RentedDao:

    def __init__(self):
        self.connection = DatabaseManager().get_connection()

    #create new rented item
    def create_rented(self, rented: CreateRented) -> int:
        transaction_id = rented.transaction_id
        media_id = rented.media_id

        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `Rented` (`transaction_id`, `media_id`) VALUES (%s, %s)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (transaction_id, media_id))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
            raise Exception("Error on create rented")
    

    #delete rented item
    def delete_rented(self, transaction_id: int) -> int:
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM `Rented` WHERE `transaction_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (transaction_id))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
    
    #get all rented items
    def get_all_rented(self) -> List[Rented]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `Rented`"
                self.connection.ping(reconnect=True)
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)
            raise Exception("Error on get all rented")
    
    #get rented item by transaction id
    def get_rented_by_transaction_id(self, transaction_id: int) -> Rented:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `Rented` WHERE `transaction_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (transaction_id))
                result = cursor.fetchone()
                return result
        except Exception as e:
            print(e)
            raise Exception("Error on get rented by transaction id")
    
    #get rented item by media id
    def get_rented_by_media_id(self, media_id: int) -> Rented:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `Rented` WHERE `media_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (media_id))
                result = cursor.fetchone()
                return result
        except Exception as e:
            print(e)
            raise Exception("Error on get rented by media id")
    
    #update rented item
    def update_rented(self, rented: UpdateRented) -> int:
        transaction_id = rented.transaction_id
        media_id = rented.media_id

        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE `Rented` SET `media_id`=%s WHERE `transaction_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (media_id, transaction_id))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
            raise Exception("Error on update rented")
    
    
