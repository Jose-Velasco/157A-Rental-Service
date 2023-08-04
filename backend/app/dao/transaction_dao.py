from app.schemas.pydantic.transaction import CreateTransaction, UpdateTransaction, Transaction
from app.models.database_manager import DatabaseManager
from app.schemas.pydantic.cart import CartSubmit
from app.dao.rented_dao import RentedDao
from typing import List
from app.schemas.pydantic.rented import CreateRented

class TransactionDao:

    def __init__(self):
        self.connection = DatabaseManager().get_connection()
    
    #create new transaction
    def create_transaction(self, cart: CartSubmit) -> dict:
        user_id = cart.user_id
        rent_duration = cart.rent_duration
        try:
            with self.connection.cursor() as cursor:
                sql = """
                       SELECT I.media_id
                       FROM Cart C, In_Cart I, Inventory IV
                       WHERE C.cart_id = I.cart_id AND I.media_id = IV.media_id AND C.user_id = %s AND IV.rent_availability_status = 1
                      """
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id))
                result = cursor.fetchall()
                media_ids = [id["media_id"] for id in result]
                for id in media_ids:
                    sql = "UPDATE Inventory SET rent_availability_status = false WHERE media_id = %s"
                    cursor.execute(sql, (id))
                sql = "INSERT INTO Transaction (user_id, rent_duration) VALUES (%s, %s)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id, rent_duration))
                if len(media_ids) == 0:
                    #no media in cart, do not create transaction, rollback and return
                    self.connection.rollback()
                    return
                self.connection.commit()
                transaction_id = cursor.lastrowid
                try:
                    for media_id in media_ids:
                        RentedDao().create_rented(CreateRented(transaction_id=transaction_id, media_id=media_id))
                except Exception as e:
                    print(e)
                try:
                    for media_id in media_ids:
                        sql = "DELETE FROM In_Cart WHERE media_id = %s"
                        self.connection.ping(reconnect=True)
                        cursor.execute(sql, (media_id))
                        self.connection.commit()
                except Exception as e:
                    print(e)
                return {'transaction_id': transaction_id, "checked out media": media_ids, "rent duration": rent_duration}

        except Exception as e:
            print(e)
            raise Exception("Error on create transaction")

    #delete transaction
    def delete_transaction(self, transaction_id: int) -> int:
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM `Transaction` WHERE `transaction_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (transaction_id))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
            raise Exception("Error on delete transaction")

    #get all transactions
    def get_all_transactions(self) -> List[Transaction]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `Transaction`"
                self.connection.ping(reconnect=True)
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)
            raise Exception("Error on get all transactions")
    
    #get transaction by id
    def get_transaction_by_id(self, transaction_id: int) -> Transaction:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `Transaction` WHERE `transaction_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (transaction_id))
                result = cursor.fetchone()
                return result
        except Exception as e:
            print(e)
            raise Exception("Error on get transaction by id")

    #update transaction
    def update_transaction(self, transaction: UpdateTransaction) -> int:
        transaction_id = transaction.transaction_id
        total_cost = transaction.total_cost
        rent_duration = transaction.rent_duration

        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE `Transaction` SET `total_cost`=%s, `rent_duration`=%s WHERE `transaction_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (total_cost, rent_duration, transaction_id))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
            raise Exception("Error on update transaction")
    
    #get all transactions for a specific user
    def get_transactions_by_user_id(self, user_id: int) -> List[Transaction]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `Transaction` WHERE `user_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id))
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)
            raise Exception("Error on get transactions by user id")
    
    