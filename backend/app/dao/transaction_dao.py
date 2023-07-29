from app.schemas.pydantic.transaction import CreateTransaction, UpdateTransaction, Transaction
from app.models.database_manager import DatabaseManager
from typing import List

class TransactionDao:

    def __init__(self):
        self.connection = DatabaseManager().get_connection()
    
    #create new transaction
    def create_transaction(self, transaction: CreateTransaction) -> int:
        user_id = transaction.user_id
        total_cost = transaction.total_cost
        rent_duration = transaction.rent_duration

        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `Transaction` (`user_id`, `total_cost`, `rent_duration`) VALUES (%s, %s, %s)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id, total_cost, rent_duration))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e.message)

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
            print(e.message)

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
            print(e.message)
    
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
            print(e.message)

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
            print(e.message)
    
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
            print(e.message)
    
    