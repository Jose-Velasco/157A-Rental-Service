from schemas.pydantic.users import Customer, CustomerCreate, CustomerUpdate
from models.database_manager import DatabaseManager

class CustomerDAO:

    def __init__(self):
        self.connection = DatabaseManager().get_connection()
    
    def create_customer(self, customer: CustomerCreate) -> int:
        first_name = customer.first_name
        last_name = customer.last_name
        birth_date = customer.birth_date
        profile_picture_url = customer.profile_picture_url
        age = customer.age
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `Customer` (`first_name`, `last_name`, `birth_date`, `profile_picture_url`, `age`) VALUES (%s, %s, %s, %s, %s)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (first_name, last_name, birth_date, profile_picture_url, age))
                self.connection.commit()
                return cursor.lastrowid
        except Exception as e:
            print(e)
            return None
            raise Exception("Error creating customer")
    
    def get_customer_by_id(self, customer_id: int) -> Customer:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `Customer` WHERE `customer_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (customer_id))
                result = cursor.fetchone()
                return Customer(**result)
        except Exception as e:
            print(e)
            return None
            raise Exception("Error getting customer by id")

    def get_all_customers(self) -> List[Customer]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `Customer`"
                self.connection.ping(reconnect=True)
                cursor.execute(sql)
                result = cursor.fetchall()
                return [Customer(**row) for row in result]
        except Exception as e:
            print(e)
            return None
            raise Exception("Error getting all customers")

    def update_customer(self, customer_id: int, customer: CustomerUpdate) -> int:
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE `Customer` SET `first_name`=%s, `last_name`=%s, `birth_date`=%s, `profile_picture_url`=%s, `age`=%s WHERE `customer_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (customer.first_name, customer.last_name, customer.birth_date, customer.profile_picture_url, customer.age, customer_id))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
            return None
            raise Exception("Error updating customer")

    def delete_customer(self, customer_id: int) -> int:
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM `Customer` WHERE `customer_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (customer_id))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
            return None
            raise Exception("Error deleting customer")
    
    

    