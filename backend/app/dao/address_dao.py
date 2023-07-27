from schemas.pydantic.address import Address, AddressCreate, AddressUpdate
from models.database_manager import DatabaseManager
from typing import List

class AddressDao:

    def __init__(self):
        self.connection = DatabaseManager().get_connection()
    
    def create_address(self, address: AddressCreate) -> int:
        user_id = address.user_id
        street = address.street
        city = address.city
        state = address.state
        zip_code = address.zip_code
        country = address.country

        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `Address` (`user_id`, `street`, `city`, `zip_code`, `state`, `country`) VALUES (%s, %s, %s, %s, %s, %s)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id, street, city, zip_code, state, country))
                self.connection.commit()

                return cursor.rowcount
        except Exception as e:
            print(e.message)
    
    def get_address_by_id(self, user_id: int) -> Address:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `Address` WHERE `user_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id))
                result = cursor.fetchall()

                return [Address(**row) for row in result]
        except Exception as e:
            print(e.message)
    
    def update_address(self, address: AddressUpdate) -> int:
        user_id = address.user_id
        street = address.street
        city = address.city
        state = address.state
        zip_code = address.zip_code
        country = address.country

        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE `Address` SET `street`=%s, `city`=%s, `state`=%s, `zip_code`=%s, `country`=%s WHERE `user_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (street, city, state, zip_code, country, user_id))
                self.connection.commit()

                return cursor.rowcount
        except Exception as e:
            print(e.message)
    
    def delete_address(self, user_id: int) -> int:
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM `Address` WHERE `user_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id))
                self.connection.commit()

                return cursor.rowcount
        except Exception as e:
            print(e.message)
    
    def get_all_addresses(self) -> List[Address]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `Address`"
                self.connection.ping(reconnect=True)
                cursor.execute(sql)
                result = cursor.fetchall()

                return [Address(**row) for row in result]
        except Exception as e:
            print(e.message)
    
    
