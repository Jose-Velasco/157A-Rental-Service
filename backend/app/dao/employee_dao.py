from schemas.pydantic.user import Employee, EmployeeCreate, EmployeeUpdate
from schemas.pydantic.address import Address, AddressCreate, AddressUpdate
from schemas.pydantic.email import Email, EmailCreate, EmailUpdate
from models.database_manager import DatabaseManager
from address_dao import AddressDao
from email_dao import EmailDao
from typing import List

class EmployeeDAO:

    def __init__(self):
        self.connection = DatabaseManager().get_connection()
    
    def create_employee(self, employee: EmployeeCreate) -> int:
        first_name = employee.first_name
        last_name = employee.last_name
        birth_date = employee.birth_date
        profile_picture_url = employee.profile_picture_url
        age = employee.age
        address_list = employee.address
        email_list = employee.email
        ssn = employee.ssn
        salary = employee.salary
        start_date = employee.start_date
        employee_type = employee.employee_type

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

                sql = "INSERT INTO `Employee` (`user_id`, `ssn`, `salary`, `start_date`, `employee_type`) VALUES (%s, %s, %s, %s, %s)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id, ssn, salary, start_date, employee_type))
                self.connection.commit()

                return cursor.rowcount
        except Exception as e:
            print(e.message)

    def get_employee_by_id(self, user_id: int) -> Employee:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `User` WHERE `user_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id))
                result = cursor.fetchone()

                address_list = AddressDao.get_address_by_id(user_id)

                email_list = EmailDao.get_email_by_id(user_id)

                sql = "SELECT * FROM `Employee` WHERE `user_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id))
                result_employee = cursor.fetchone()
                employee = Employee(**result, address=address_list, email=email_list, **result_employee)

                return employee
        except Exception as e:
            print(e.message)
    
    def get_all_employees(self) -> List[Employee]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `User` WHERE `user_id` IN (SELECT `user_id` FROM `Employee`)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql)
                result = cursor.fetchall()

                employee_list = []
                for row in result:
                    address_list = AddressDao.get_address_by_id(row['user_id'])

                    email_list = EmailDao.get_email_by_id(row['user_id'])

                    sql = "SELECT * FROM `Employee` WHERE `user_id`=%s"
                    self.connection.ping(reconnect=True)
                    cursor.execute(sql, (row['user_id']))
                    result_employee = cursor.fetchone()
                    employee = Employee(**row, address=address_list, email=email_list, **result_employee)
                    employee_list.append(employee)
                return employee_list
        except Exception as e:
            print(e.message)