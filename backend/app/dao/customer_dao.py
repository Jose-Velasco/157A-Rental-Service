from app.schemas.pydantic.user import Customer, CustomerCreate, CustomerUpdate
from app.schemas.pydantic.address import Address, AddressCreate, AddressUpdate
from app.schemas.pydantic.email import Email, EmailCreate, EmailUpdate
from app.models.database_manager import DatabaseManager
from app.dao.address_dao import AddressDao
from app.dao.email_dao import EmailDao
from typing import List
from app.auth.auth import get_pass_hash

class CustomerDAO:

    def __init__(self):
        self.connection = DatabaseManager().get_connection()
    
    def create_customer(self, customer: CustomerCreate) -> int:
        first_name = customer.first_name
        last_name = customer.last_name
        birth_date = customer.birthday
        profile_pic_URL = customer.profile_pic_URL
        age = customer.age
        address_list = customer.address
        email_list = customer.email
        phone_number = customer.phone_number
        username = customer.username
        hashed_password = get_pass_hash(customer.password)

        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `User` (`first_name`, `last_name`, `birthday`, `profile_pic_URL`, `age`, `phone_number`) VALUES (%s, %s, %s, %s, %s, %s)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (first_name, last_name, birth_date, profile_pic_URL, age, phone_number))
                self.connection.commit()
                user_id = cursor.lastrowid

                sql = "INSERT INTO `Auth` (`user_id`, `username`, `hashed_password`) VALUES (%s, %s, %s)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id, username, hashed_password))
                self.connection.commit()

                for address in address_list:
                    address = AddressCreate(user_id=user_id, street=address.street, city=address.city, zip_code=address.zip_code, state=address.state, country=address.country, phone_number=phone_number)
                    print(address)
                    AddressDao().create_address(address)

                for email in email_list:
                    email = EmailCreate(user_id=user_id, email=email.email)
                    print(email)
                    EmailDao().create_email(email)
                

                return cursor.rowcount
        except Exception as e:
            print(e)
            raise Exception("Error on create customer")
            

        
    
    def get_customer_by_id(self, user_id: int) -> Customer:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `User` WHERE `user_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id))
                result = cursor.fetchone()

                address_list = AddressDao().get_address_by_id(user_id)

                email_list = EmailDao().get_email_by_id(user_id)

                return Customer(user_id=result['user_id'], first_name=result['first_name'], last_name=result['last_name'], birthday=result['birthday'], profile_pic_URL=result['profile_pic_URL'], age=result['age'], phone_number=result['phone_number'], address=address_list, email=email_list)
                
        except Exception as e:
            print(e)
            raise Exception("Error on get customer by id")
            

    def get_all_customers(self) -> List[Customer]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `User` WHERE `user_id` NOT IN (SELECT `user_id` FROM `Employee`)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql)
                result = cursor.fetchall()
                
                customer_list = []
                for row in result:
                    address_list = AddressDao().get_address_by_id(row['user_id'])
                    email_list = EmailDao().get_email_by_id(row['user_id'])
                    customer_list.append(Customer(user_id=row['user_id'], first_name=row['first_name'], last_name=row['last_name'], birthday=row['birthday'], profile_pic_URL=row['profile_pic_URL'], age=row['age'], phone_number=row['phone_number'], address=address_list, email=email_list))
                    

                return customer_list
        except Exception as e:
            print(e)
            raise Exception("Error on get all customers")
            

    def update_customer(self, user_id: int, customer: CustomerUpdate) -> int:
        try:
            with self.connection.cursor() as cursor:
                print(customer)
                sql = "UPDATE `User` SET `first_name`=%s, `last_name`=%s, `birthday`=%s, `profile_pic_URL`=%s, `age`=%s, `phone_number`=%s WHERE `user_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (customer.first_name, customer.last_name, customer.birthday, customer.profile_pic_URL, customer.age, customer.phone_number, user_id))
                self.connection.commit()

                for address in customer.address:
                    AddressDao().update_address(user_id=user_id, address=address)
                
                for email in customer.email:
                    EmailDao().update_email(user_id=user_id, email=email)

                return cursor.rowcount
        except Exception as e:
            print(e)
            raise Exception("Error on update customer")
            

    def delete_customer(self, user_id: int) -> int:
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM `User` WHERE `user_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
            raise Exception("Error on delete customer")
            
    
    

    