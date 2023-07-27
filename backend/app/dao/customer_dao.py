from schemas.pydantic.user import Customer, CustomerCreate, CustomerUpdate
from schemas.pydantic.address import Address, AddressCreate, AddressUpdate
from schemas.pydantic.email import Email, EmailCreate, EmailUpdate
from models.database_manager import DatabaseManager
from address_dao import AddressDao
from email_dao import EmailDao
from typing import List

class CustomerDAO:

    def __init__(self):
        self.connection = DatabaseManager().get_connection()
    
    def create_customer(self, customer: CustomerCreate) -> int:
        first_name = customer.first_name
        last_name = customer.last_name
        birth_date = customer.birth_date
        profile_picture_url = customer.profile_picture_url
        age = customer.age
        address_list = customer.address
        email_list = customer.email

        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `User` (`first_name`, `last_name`, `birth_date`, `profile_picture_url`, `age`) VALUES (%s, %s, %s, %s, %s)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (first_name, last_name, birth_date, profile_picture_url, age))
                self.connection.commit()
                user_id = cursor.lastrowid

                for address in address_list:
                    AddressDao.create_address(AddressCreate(user_id=user_id, street=address.street, city=address.city, zip_code=address.zip_code, state=address.state, country=address.country))

                for email in email_list:
                    EmailDao.create_email(EmailCreate(user_id=user_id, email_address=email.email))

                return cursor.rowcount
        except Exception as e:
            print(e.message)
            

        
    
    def get_customer_by_id(self, user_id: int) -> Customer:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `User` WHERE `user_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id))
                result = cursor.fetchone()

                address_list = AddressDao.get_address_by_id(user_id)

                email_list = EmailDao.get_email_by_id(user_id)

                return Customer(**result, address=address_list, email=email_list)
                
        except Exception as e:
            print(e.message)
            

    def get_all_customers(self) -> List[Customer]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `User` WHERE `user_id` NOT IN (SELECT `user_id` FROM `Employee`)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql)
                result = cursor.fetchall()
                
                customer_list = []
                for row in result:
                    address_list = AddressDao.get_address_by_id(row['user_id'])
                    email_list = EmailDao.get_email_by_id(row['user_id'])
                    customer_list.append(Customer(**row, address=address_list, email=email_list))

                return customer_list
        except Exception as e:
            print(e)
            return None
            raise Exception("Error getting all customers")

    def update_customer(self, user_id: int, customer: CustomerUpdate) -> int:
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE `User` SET `first_name`=%s, `last_name`=%s, `birth_date`=%s, `profile_picture_url`=%s, `age`=%s WHERE `user_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (customer.first_name, customer.last_name, customer.birth_date, customer.profile_picture_url, customer.age, user_id))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e.message)
            

    def delete_customer(self, user_id: int) -> int:
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM `User` WHERE `user_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e.message)
            
    
    

    