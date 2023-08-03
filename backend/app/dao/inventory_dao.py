from app.schemas.pydantic.inventory import InventoryCreate, InventoryUpdate, Inventory
from app.models.database_manager import DatabaseManager
from typing import List

class InventoryDAO:
    
    def __init__(self):
        self.connection = DatabaseManager().get_connection()

    #create new inventory item
    def create_inventory(self, inventory: InventoryCreate) -> int:
        media_id = inventory.media_id
        rent_availability_status = inventory.rent_availability_status

        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `Inventory` (`media_id`, `rent_availability_status`) VALUES (%s, %s)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (media_id, rent_availability_status))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
            raise Exception("Error on create inventory")
    
    #delete inventory item
    def delete_inventory(self, media_id: int) -> int:
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM `Inventory` WHERE `media_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (media_id))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
            raise Exception("Error on delete inventory")
    
    #get all available inventory items
    def get_available_inventory(self) -> List[Inventory]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `Inventory` WHERE `rent_availability_status`=1"
                self.connection.ping(reconnect=True)
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)
            raise Exception("Error on get available inventory")
    
    #get all items
    def get_all_inventory(self) -> List[Inventory]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `Inventory`"
                self.connection.ping(reconnect=True)
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)
            raise Exception("Error on get all inventory")

    #check if inventory item is available
    def check_availability(self, media_id: int) -> bool:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT `rent_availability_status` FROM `Inventory` WHERE `media_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (media_id))
                result = cursor.fetchone()
                return result['rent_availability_status']
        except Exception as e:
            print(e)
            raise Exception("Error on check availability")
    
    #update inventory item
    def update_inventory(self, inventory: InventoryUpdate) -> int:
        media_id = inventory.media_id
        rent_availability_status = inventory.rent_availability_status

        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE `Inventory` SET `rent_availability_status`=%s WHERE `media_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (rent_availability_status, media_id))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
            raise Exception("Error on update inventory")
    
    